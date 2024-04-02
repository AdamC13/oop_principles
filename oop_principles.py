class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, category_name):
        if type(category_name) == str:
            self.__category_name = category_name

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, allocated_budget):
        if (type(allocated_budget) == int or type(allocated_budget) == float) and allocated_budget >= 0:
            self.__allocated_budget = allocated_budget


    def add_expense(self, amount):
        if (type(amount) == int or type(amount) == float) and amount + self.__expenses <= self.__allocated_budget:
            self.__expenses += amount
        else:
            return False



    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print(f"You have ${remaining_budget}'s left of your ${self.__allocated_budget} budget for {self.__category_name}.")


# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()