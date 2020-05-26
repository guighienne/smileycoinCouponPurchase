import ecdsa
import binascii
import hashlib
import struct
import hashlib
import utils
import base58

def wifToPrivateKey(s):
    return base58.b58decode(s)

if str != bytes:
	def ord(c):
		return c
	def chr(n):
		return bytes( (n,) )

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def address_to_script(v):
    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += __b58chars.find(c) * (__b58base**i)
    result = bytes()
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = chr(mod) + result
        long_value = div
    result = chr(long_value) + result
    nPad = 0
    for c in v:
        if c == __b58chars[0]: nPad += 1
        else: break
    result = chr(0)*nPad + result
    result = binascii.hexlify(result)[2:-8].decode("utf-8")
    return result


# Makes a transaction from the inputs
# outputs is a list of [redemptionSatoshis, outputScript]

def makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs):
    def makeOutput(data):
        redemptionSatoshis, outputScript = data
        return (struct.pack("<Q", redemptionSatoshis).encode('hex') +
        '%02x' % len(outputScript.decode('hex')) + outputScript)
    formattedOutputs = ''.join(map(makeOutput, outputs))
    return (
        "01000000" + # 4 bytes version
        "01" + # varint for number of inputs
        outputTransactionHash.decode('hex')[::-1].encode('hex') + # reverse outputTransactionHash
        struct.pack('<L', sourceIndex).encode('hex') +
        '%02x' % len(scriptSig.decode('hex')) + scriptSig +
        "ffffffff" + # sequence
        "%02x" % len(outputs) + # number of outputs
        formattedOutputs +
        "00000000" # lockTime
        )

def makeSignedTransaction(privateKey, outputTransactionHash, sourceIndex, scriptPubKey,scriptSig,coupon, outputs):
    if coupon==' encrypted coupon (for seller only)':
        coupon=''
    else:
        coupon='4d'+str('%04x'%len(coupon.decode('hex'))).decode('hex')[::-1].encode('hex')+coupon
    myTxn_forSig = (makeRawTransaction(outputTransactionHash, sourceIndex, scriptPubKey, outputs)
         + "01000000")
    privateKey=wifToPrivateKey(privateKey)
    s256 = hashlib.sha256(hashlib.sha256(myTxn_forSig.decode('hex')).digest()).digest()
    sk = ecdsa.SigningKey.from_string(privateKey.decode('hex'), curve=ecdsa.SECP256k1)
    sig = sk.sign_digest(s256, sigencode=ecdsa.util.sigencode_der) + '\01' # 01 is hashtype
    scriptSig = '%02x'%len(sig)+sig.encode('hex') +coupon+scriptSig
    signed_txn = makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs)
    return signed_txn

def transaction3_scriptPubKey(tx2,clientPubKey):
    pos=86+int(tx2[84:86],16)*2
    sellerPubKey=tx2[pos:pos+int(tx2[pos:pos+2],16)*2+2]
    pos=94+int(tx2[82:84],16)*2
    for vout in range(int(tx2[pos-2:pos])):
        if tx2[pos+18:pos+20]=='6a':
            hash=tx2[pos+20:pos+20+int(tx2[pos+20:pos+22],16)*2+2]
            break
        else:
            pos+=18+int(tx2[pos+16:pos+18],16)*2
            hash=None
    scriptPubKey='6321'+clientPubKey+'ad67a9'+hash+'87'+sellerPubKey+'ad68'
    return scriptPubKey

def transaction2_getPubKey(tx):
    pos=86+int(tx[84:86],16)*2
    return tx[pos+2:pos+int(tx[pos:pos+2],16)*2+2]

def redeem_data(tx):
    pos=94+int(tx[82:84],16)*2
    script,pub,sm='','',''
    for vout in range(int(tx[pos-2:pos])):
        ### for P2SH
        # if tx[pos+18:pos+20]=='6a':
        #     script=tx[pos+20:pos+20+int(tx[pos+20:pos+22],16)*2+2]
        # elif tx[pos+18:pos+20]=='a9':
        if tx[pos+18:pos+20]=='63':
            pub=tx[pos+18:pos+20+int(tx[pos+20:pos+22],16)*2+2]
            sm=int(tx[pos:pos+16].decode('hex')[::-1].encode('hex'),16)-100000000
        pos+=18+int(tx[pos+16:pos+18],16)*2
    return [script,pub,sm]

#print redeem_data('0100000001161a7ca08ab3ba70c10da25ad36a6bec8affd132b7402253913c552f6919f218010000006a47304402204d8d291797e519ed5b0b8312f9a321c4b611c34c0c493fc651cf868d563612d8022015646209097f1677434be877321593a013253a951bac9c75558eaf792b1aa9dc01210360f7cf38f0537751ec6c078dc65c1bb4e0a42bf6d9884d3907dff855957eb745ffffffff04008eead0010000001976a91467b854912b3717f506514ce48e67f377d721da0588ac00e1f505000000001976a914cde346fb53db66c96c74897969945f4fa76c6c8f88ac009435770000000017a91420f0f54fa4e2fa1e6dd8704c095a54d4b5fcf40d870000000000000000626a606321025c8b1194510c622cb191a0a7e0f85357c561264c88a34a172c972f2bee959759ad67a914bf5e357b7f4d51ed0524f5c5d2eab6d98147be5187210360f7cf38f0537751ec6c078dc65c1bb4e0a42bf6d9884d3907dff855957eb745ad6800000000')

