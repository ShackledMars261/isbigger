# is_bigger

## Normal
```
from is_bigger.functions import *

isBigger(2,1) # True
isSmaller(2,1) # False
isEqual(3,3) # True
isNotBigger(3,1) # False
isNotSmaller(3,1) # True
isNotEqual(3,1) # True
```

## Machine Learning (slower and doesn't always work)
```
from is_bigger.mlfunctions import *

ml_is_bigger(3,2) # True
ml_is_smaller(2,3) # True
ml_is_equal(1,1) # True
ml_is_not_bigger(2,2) # True
ml_is_not_smaller(3,2) # True
ml_is_not_equal(4,4) # False
```