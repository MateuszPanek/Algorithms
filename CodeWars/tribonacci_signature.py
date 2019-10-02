def tribonacci(signature:list, n:int) -> list:
    """Generates Tribonacci sequence out of given signature and length"""
    for i in range(n - 3):
        signature.append(sum(signature[i:i + 3]))
    return signature[:n]
