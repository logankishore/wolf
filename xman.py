if __name__ == '__main__':
    print(Crypto().encrypt("0i6QnSETFywG4Opne/WlKbud/krcUhtxZKPo5iFzh6o="))
    print(Crypto().decrypt("ygfJhsgEhebdhWrdcf3f=="))
    print(CryptoPMP(meta={"decrypt_key": "ygfJhsgEhebdhWrdcf3f=="}).decrypt("hjIauAbgtiHGFsEvna=="))
