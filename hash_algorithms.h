#ifndef hash_algorithms_h
#define hash_algorithms_h

#include "openssl/sha.h"
#include "openssl/md5.h"

#include <vector>

class HashAlgorithms
{
public:
    HashAlgorithms() {};
    virtual ~HashAlgorithms() {};

    virtual void update(const void* buffer, size_t buffer_size) = 0;
    virtual std::vector<uint8_t> GetResult() = 0;
};

class SHA512_Hash : public HashAlgorithms
{
public:
    SHA512_Hash() { SHA512_Init(&sha512_context); };
    ~SHA512_Hash() {};

    void update(const void* buffer, size_t buffer_size)
    {
        SHA512_Update(&sha512_context, buffer, buffer_size);
    };

    std::vector<uint8_t> GetResult()
    {
        SHA512_Final(array_result, &sha512_context);
        std::vector<uint8_t> result(array_result, array_result + SHA512_DIGEST_LENGTH);
        return result;
    };

private:
    SHA512_CTX sha512_context;
    uint8_t array_result[SHA512_DIGEST_LENGTH] = { 0 };
};



class SHA256_Hash : public HashAlgorithms
{
public:
    SHA256_Hash() { SHA256_Init(&sha256_context); };
    ~SHA256_Hash() {};

    void update(const void* buffer, size_t buffer_size)
    {
        SHA256_Update(&sha256_context, buffer, buffer_size);
    };

    std::vector<uint8_t> GetResult()
    {
        SHA256_Final(array_result, &sha256_context);
        std::vector<uint8_t> result(array_result, array_result + SHA256_DIGEST_LENGTH);
        return result;
    };

private:
    SHA256_CTX sha256_context;
    uint8_t array_result[SHA256_DIGEST_LENGTH] = { 0 };
};



class MD5_Hash : public HashAlgorithms
{
public:
    MD5_Hash() { MD5_Init(&md5_context); };
    ~MD5_Hash() {};

    void update(const void* buffer, size_t buffer_size)
    {
        MD5_Update(&md5_context, buffer, buffer_size);
    };

    std::vector<uint8_t> GetResult()
    {
        MD5_Final(array_result, &md5_context);
        std::vector<uint8_t> result(array_result, array_result + MD5_DIGEST_LENGTH);
        return result;
    };

private:
    MD5_CTX md5_context;
    uint8_t array_result[MD5_DIGEST_LENGTH] = { 0 };
};

#endif