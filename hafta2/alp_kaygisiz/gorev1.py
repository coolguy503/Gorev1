def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    sayilar = [2, 7, 11, 15]
    hedef = 9
    sonuc = two_sum(sayilar, hedef)
    print(f"Liste: {sayilar}, Hedef: {hedef} -> İndeksler: {sonuc}")
