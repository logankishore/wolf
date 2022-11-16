if __name__ == '__main__':
    print(Crypto().encrypt("NG70d9w"))
    print(Crypto().decrypt("ygfJhsgEhebdhWrdcf3f=="))
    print(CryptoPMP(meta={"decrypt_key": "ygfJhsgEhebdhWrdcf3f=="}).decrypt("hjIauAbgtiHGFsEvna=="))
