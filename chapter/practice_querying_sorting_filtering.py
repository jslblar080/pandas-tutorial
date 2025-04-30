import seaborn as sns

from base_chapter import BaseChapter


class PracticeQueryingSortingFiltering(BaseChapter):

    def __init__(self):
        super(PracticeQueryingSortingFiltering, self).__init__()
        print("조회, 정렬, 필터 연습\n")

    def play(self) -> None:
        df = sns.load_dataset("titanic")
        print(df.head(), '\n')
        """
           survived  pclass     sex   age  ...  deck  embark_town  alive  alone
        0         0       3    male  22.0  ...   NaN  Southampton     no  False
        1         1       1  female  38.0  ...     C    Cherbourg    yes  False
        2         1       3  female  26.0  ...   NaN  Southampton    yes   True
        3         1       1  female  35.0  ...     C  Southampton    yes  False
        4         0       3    male  35.0  ...   NaN  Southampton     no   True

        [5 rows x 15 columns]
        """
        print(df["embark_town"].value_counts(), '\n')
        """
        embark_town
        Southampton    644
        Cherbourg      168
        Queenstown      77
        Name: count, dtype: int64
        """
        print(df["who"].value_counts(), '\n')
        """
        who
        man      537
        woman    271
        child     83
        Name: count, dtype: int64 
        """

        tips = sns.load_dataset("tips")
        print(tips.head(), '\n')
        """
           total_bill   tip     sex smoker  day    time  size
        0       16.99  1.01  Female     No  Sun  Dinner     2
        1       10.34  1.66    Male     No  Sun  Dinner     3
        2       21.01  3.50    Male     No  Sun  Dinner     3
        3       23.68  3.31    Male     No  Sun  Dinner     2
        4       24.59  3.61  Female     No  Sun  Dinner     4
        """
        print(tips.sort_values(by=["total_bill", "tip"], ascending=[False, False]).head(10), '\n')
        """
             total_bill    tip     sex smoker   day    time  size
        170       50.81  10.00    Male    Yes   Sat  Dinner     3
        212       48.33   9.00    Male     No   Sat  Dinner     4
        59        48.27   6.73    Male     No   Sat  Dinner     4
        156       48.17   5.00    Male     No   Sun  Dinner     6
        182       45.35   3.50    Male    Yes   Sun  Dinner     3
        102       44.30   2.50  Female    Yes   Sat  Dinner     3
        197       43.11   5.00  Female    Yes  Thur   Lunch     4
        142       41.19   5.00    Male     No  Thur   Lunch     5
        184       40.55   3.00    Male    Yes   Sun  Dinner     2
        95        40.17   4.73    Male    Yes   Fri  Dinner     4
        """
        print(tips.sort_values(by=["size", "tip"], ascending=[False, True]).head(10), '\n')
        """
             total_bill   tip     sex smoker   day    time  size
        125       29.80  4.20  Female     No  Thur   Lunch     6
        143       27.05  5.00  Female     No  Thur   Lunch     6
        156       48.17  5.00    Male     No   Sun  Dinner     6
        141       34.30  6.70    Male     No  Thur   Lunch     6
        187       30.46  2.00    Male    Yes   Sun  Dinner     5
        216       28.15  3.00    Male    Yes   Sat  Dinner     5
        142       41.19  5.00    Male     No  Thur   Lunch     5
        185       20.69  5.00    Male     No   Sun  Dinner     5
        155       29.85  5.14  Female     No   Sun  Dinner     5
        153       24.55  2.00    Male     No   Sun  Dinner     4
        """

        print(df.iloc[3:8, ], '\n')
        """
           survived  pclass     sex   age  ...  deck  embark_town  alive  alone
        3         1       1  female  35.0  ...     C  Southampton    yes  False
        4         0       3    male  35.0  ...   NaN  Southampton     no   True
        5         0       3    male   NaN  ...   NaN   Queenstown     no   True
        6         0       1    male  54.0  ...     E  Southampton     no   True
        7         0       3    male   2.0  ...   NaN  Southampton     no  False

        [5 rows x 15 columns] 
        """
        print(df.loc[:4, "pclass":"fare"], '\n')
        """
           pclass     sex   age  sibsp  parch     fare
        0       3    male  22.0      1      0   7.2500
        1       1  female  38.0      1      0  71.2833
        2       3  female  26.0      0      0   7.9250
        3       1  female  35.0      1      0  53.1000
        4       3    male  35.0      0      0   8.0500
        """
        print(df.loc[range(2, 12, 2), ["age", "who"]], '\n')
        """
             age    who
        2   26.0  woman
        4   35.0    man
        6   54.0    man
        8   27.0  woman
        10   4.0  child
        """
        cond = (df["age"] >= 30) & (df["sex"] == "male")
        print(df[cond].sort_values(by="fare", ascending=False).head(10), '\n')
        """
             survived  pclass   sex   age  ...  deck  embark_town  alive  alone
        679         1       1  male  36.0  ...     B    Cherbourg    yes  False
        737         1       1  male  35.0  ...     B    Cherbourg    yes   True
        438         0       1  male  64.0  ...     C  Southampton     no  False
        332         0       1  male  38.0  ...     C  Southampton     no  False
        660         1       1  male  50.0  ...   NaN  Southampton    yes  False
        390         1       1  male  36.0  ...     B  Southampton    yes  False
        659         0       1  male  58.0  ...     D    Cherbourg     no  False
        698         0       1  male  49.0  ...     C    Cherbourg     no  False
        544         0       1  male  50.0  ...     C    Cherbourg     no  False
        245         0       1  male  44.0  ...     C   Queenstown     no  False
        
        [10 rows x 15 columns]
        """
        cond = (df["age"] >= 20) & (df["age"] < 40) & (df["pclass"].isin([1, 2]))
        print(df.loc[cond, ["survived", "pclass", "age", "fare"]].head(10), '\n')
        """
            survived  pclass   age     fare
        1          1       1  38.0  71.2833
        3          1       1  35.0  53.1000
        20         0       2  35.0  26.0000
        21         1       2  34.0  13.0000
        23         1       1  28.0  35.5000
        34         0       1  28.0  82.1708
        41         0       2  27.0  21.0000
        53         1       2  29.0  26.0000
        56         1       2  21.0  10.5000
        61         1       1  38.0  80.0000
        """

        cond = tips["day"].isin(["Fri", "Sat"]) & (tips["tip"] < 10)
        print(tips.loc[cond, ["total_bill", "tip", "smoker", "time"]].head(10))
        """
            total_bill   tip smoker    time
        19       20.65  3.35     No  Dinner
        20       17.92  4.08     No  Dinner
        21       20.29  2.75     No  Dinner
        22       15.77  2.23     No  Dinner
        23       39.42  7.58     No  Dinner
        24       19.82  3.18     No  Dinner
        25       17.81  2.34     No  Dinner
        26       13.37  2.00     No  Dinner
        27       12.69  2.00     No  Dinner
        28       21.70  4.30     No  Dinner
        """
