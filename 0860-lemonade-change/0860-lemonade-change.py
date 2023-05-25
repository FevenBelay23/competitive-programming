class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_bills = 0
        ten_dollar_bills = 0
        for i in bills:
            if i == 5:
                five_dollar_bills += 1
            elif i == 10:
                if five_dollar_bills == 0:
                    return False
                ten_dollar_bills += 1
                five_dollar_bills -= 1
            else:
                if (five_dollar_bills >= 1 and ten_dollar_bills >=1):
                    five_dollar_bills -= 1
                    ten_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    return False
        return True
        