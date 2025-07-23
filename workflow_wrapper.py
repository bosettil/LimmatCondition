import os
from LimmatCondition import check_limmat_condition

if __name__ == "__main__":
    print(os.getcwd())
    check_limmat_condition(fig_path='./figures/limmat_condition.png')
