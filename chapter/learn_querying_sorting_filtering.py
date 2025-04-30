import seaborn as sns

from base_chapter import BaseChapter


class LearnQueryingSortingFiltering(BaseChapter):

    def __init__(self):
        super(LearnQueryingSortingFiltering, self).__init__()
        print("조회, 정렬, 필터 학습\n")

    def play(self) -> None:
        df = sns.load_dataset("titanic")

        # Querying
        print(df.head(3))
        """
           survived  pclass     sex   age  ...  deck  embark_town  alive  alone
        0         0       3    male  22.0  ...   NaN  Southampton     no  False
        1         1       1  female  38.0  ...     C    Cherbourg    yes  False
        2         1       3  female  26.0  ...   NaN  Southampton    yes   True

        [3 rows x 15 columns]
        """
        print(df.tail(7))
        """
            survived  pclass     sex   age  ...  deck  embark_town  alive  alone
        884         0       3    male  25.0  ...   NaN  Southampton     no   True
        885         0       3  female  39.0  ...   NaN   Queenstown     no  False
        886         0       2    male  27.0  ...   NaN  Southampton     no   True
        887         1       1  female  19.0  ...     B  Southampton    yes   True
        888         0       3  female   NaN  ...   NaN  Southampton     no  False
        889         1       1    male  26.0  ...     C    Cherbourg    yes   True
        890         0       3    male  32.0  ...   NaN   Queenstown     no   True

        [7 rows x 15 columns]
        """
        print(df.info())
        """
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 891 entries, 0 to 890
        Data columns (total 15 columns):
        #   Column       Non-Null Count  Dtype   
        ---  ------       --------------  -----   
        0   survived     891 non-null    int64   
        1   pclass       891 non-null    int64   
        2   sex          891 non-null    object  
        3   age          714 non-null    float64 
        4   sibsp        891 non-null    int64   
        5   parch        891 non-null    int64   
        6   fare         891 non-null    float64 
        7   embarked     889 non-null    object  
        8   class        891 non-null    category
        9   who          891 non-null    object  
        10  adult_male   891 non-null    bool    
        11  deck         203 non-null    category
        12  embark_town  889 non-null    object  
        13  alive        891 non-null    object  
        14  alone        891 non-null    bool    
        dtypes: bool(2), category(2), float64(2), int64(4), object(5)
        memory usage: 80.7+ KB
        None
        """
        print(df["who"].value_counts())
        """
        who
        man      537
        woman    271
        child     83
        Name: count, dtype: int64
        """
        ## Attributes
        print(df.ndim)
        """
        2
        """
        print(df.shape)
        """
        (891, 15)
        """
        print(df.index)
        """
        RangeIndex(start=0, stop=891, step=1)
        """
        print(df.columns)
        """
        Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
        'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
        'alive', 'alone'],
        dtype='object')
        """
        print(df.values)
        """
        [[0 3 'male' ... 'Southampton' 'no' False]
        [1 1 'female' ... 'Cherbourg' 'yes' False]
        [1 3 'female' ... 'Southampton' 'yes' True]
        ...
        [0 3 'female' ... 'Southampton' 'no' False]
        [1 1 'male' ... 'Cherbourg' 'yes' True]
        [0 3 'male' ... 'Queenstown' 'no' True]]
        """
        print(df.T)
        """
                             0          1    ...        889         890
        survived               0          1  ...          1           0
        pclass                 3          1  ...          1           3
        sex                 male     female  ...       male        male
        age                 22.0       38.0  ...       26.0        32.0
        sibsp                  1          1  ...          0           0
        parch                  0          0  ...          0           0
        fare                7.25    71.2833  ...       30.0        7.75
        embarked               S          C  ...          C           Q
        class              Third      First  ...      First       Third
        who                  man      woman  ...        man         man
        adult_male          True      False  ...       True        True
        deck                 NaN          C  ...          C         NaN
        embark_town  Southampton  Cherbourg  ...  Cherbourg  Queenstown
        alive                 no        yes  ...        yes          no
        alone              False      False  ...       True        True

        [15 rows x 891 columns]
        """
        print(df["pclass"].astype("str").head())
        """
        0    3
        1    1
        2    3
        3    1
        4    3
        Name: pclass, dtype: object
        """
        print(df["pclass"].astype("category").head())
        """
        0    3
        1    1
        2    3
        3    1
        4    3
        Name: pclass, dtype: category
        Categories (3, int64): [1, 2, 3]
        """

        # Sorting
        print(df.sort_index(ascending=False).head(5))
        """
             survived  pclass     sex   age  ...  deck  embark_town  alive  alone
        890         0       3    male  32.0  ...   NaN   Queenstown     no   True
        889         1       1    male  26.0  ...     C    Cherbourg    yes   True
        888         0       3  female   NaN  ...   NaN  Southampton     no  False
        887         1       1  female  19.0  ...     B  Southampton    yes   True
        886         0       2    male  27.0  ...   NaN  Southampton     no   True

        [5 rows x 15 columns]
        """
        print(df[["fare", "age"]].sort_values(by=["fare", "age"], ascending=[False, True]).head())
        """
                 fare   age
        258  512.3292  35.0
        737  512.3292  35.0
        679  512.3292  36.0
        27   263.0000  19.0
        88   263.0000  23.0
        """

        # Filtering
        print(df.loc[5, "class"])
        """
        Third
        """
        print(df.loc[:6, "class":"deck"])
        """
           class    who  adult_male deck
        0  Third    man        True  NaN
        1  First  woman       False    C
        2  Third  woman       False  NaN
        3  First  woman       False    C
        4  Third    man        True  NaN
        5  Third    man        True  NaN
        6  First    man        True    E
        """
        print(df["age"] >= 70)
        """
        0      False
        1      False
        2      False
        3      False
        4      False
                ...  
        886    False
        887    False
        888    False
        889    False
        890    False
        Name: age, Length: 891, dtype: bool
        """
        print(df.loc[df["age"] >= 70])
        """
             survived  pclass   sex   age  ...  deck  embark_town  alive  alone
        96          0       1  male  71.0  ...     A    Cherbourg     no   True
        116         0       3  male  70.5  ...   NaN   Queenstown     no   True
        493         0       1  male  71.0  ...   NaN    Cherbourg     no   True
        630         1       1  male  80.0  ...     A  Southampton    yes   True
        672         0       2  male  70.0  ...   NaN  Southampton     no   True
        745         0       1  male  70.0  ...     B  Southampton     no  False
        851         0       3  male  74.0  ...   NaN  Southampton     no   True

        [7 rows x 15 columns]
        """
        print(df.loc[df["age"] >= 70], "age")
        """
             survived  pclass   sex   age  ...  deck  embark_town  alive  alone
        96          0       1  male  71.0  ...     A    Cherbourg     no   True
        116         0       3  male  70.5  ...   NaN   Queenstown     no   True
        493         0       1  male  71.0  ...   NaN    Cherbourg     no   True
        630         1       1  male  80.0  ...     A  Southampton    yes   True
        672         0       2  male  70.0  ...   NaN  Southampton     no   True
        745         0       1  male  70.0  ...     B  Southampton     no  False
        851         0       3  male  74.0  ...   NaN  Southampton     no   True

        [7 rows x 15 columns] age
        """
        cond1 = df["age"] >= 70
        cond2 = df["embark_town"].isin(["Cherbourg", "Queenstown"])
        print(df.loc[cond1 & cond2])
        """
             survived  pclass   sex   age  ...  deck  embark_town  alive alone
        96          0       1  male  71.0  ...     A    Cherbourg     no  True
        116         0       3  male  70.5  ...   NaN   Queenstown     no  True
        493         0       1  male  71.0  ...   NaN    Cherbourg     no  True
        """
        print(df.iloc[:3, :5])
        """
           survived  pclass     sex   age  sibsp
        0         0       3    male  22.0      1
        1         1       1  female  38.0      1
        2         1       3  female  26.0      0
        """
