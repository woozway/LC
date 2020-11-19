class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """
        or you can use 'Kim larsen calculation formula'
        """
        return datetime.date(year, month, day).strftime('%A')
