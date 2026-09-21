

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
      products: list[int] =  [0] * len(nums)
      left_products : list[int] = []
      right_product : list[int] = [0] * len(nums)
      last_product = 1

      for index , num in enumerate(nums):
        left_products.append(last_product)
        last_product *= num

      last_product = 1
      for index in range(len(nums)-1, -1 , -1):
        right_product[index] = last_product
        last_product = last_product * nums[index]

      for index in range(len(left_products)):
        products[index] = left_products[index] * right_product[index]

      return products
