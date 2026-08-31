# qounter
A tool to search for all possible components of a given list of numbers to add to a specific partial sum.

## How to use
### Installation
Download the code (and extract the .zip if necessary). You will find two python files, `qounter.py` and `quonter-gui.py`, a CLI and a GUI application. To run these programs you will need a version of **python 3.14** which you can either install via a package manager on Linux or [with an installer](https://www.python.org/downloads/windows/) for Windows. On Linux you might have to install the **tkinter python package** for *python 3.14*, on Windows it should be included in the installer.

### How to use the GUI
Opening the GUI you will see 4 main options:
- "open file" will open a file explorer in which you can choose a **.csv table** to use as an input list
- "sum" is the sum which you are searching the addends for
- "margin" allows to show solutions that are slightly off sum (this is optional)
- "calculate" will start the calculation of possible addends that add to sum (+/- margin)
![Window example with more explanation][tut-win]
> It might take a while if there are a lot of possible solutions.
> You can see all solutions listed out in the console. The addends will be in the same order as they were in the input list.

When exporting the .csv put the addends in the first column with either an empty cell or a cell with anything other than a number at the end:
![Table example to show what will be read][tut-tbl]

### How to use the CLI
**usage**: `qounter.py [-h] [-f path] [-s float] [-m float]`
**options**:
```
  -h, --help          show this help message and exit
  -f, --file path     path to CSV input data
  -s, --sum float     partial sum that needs to be calculated using the
                      elements from the input data
  -m, --margin float  +/- margin the sum can be off by (optional)
```

## Thought process

### 1. The Problem
We have a list `L` of `n` addends. `t` is the total sum of all elements of `L`. An unknown qantity `m` of addends sum to a partial sum `p <= t`. Addends in `L` don't have to be unique but can only be used once to calculate `p`. `p` can be made out of an arbitrary amount `0 to n` addends.
With only knowing `L` and `p` how can we find out all addends `p` is made of?

Example:
```
| L      |
| ------ |
| 45.87  |
| 67.88  |
| 67.96  |
| 67.02  |
| 128.89 |
| 200.74 |
| 140.25 |
| 69.69  |
| 100.37 |
| 40.7   |
| 500.59 |
| 30.45  |
| 45.89  |

p = 421.24
t = 1506.3
```
-> What is a solution to `p` using only elements of `L` while using every element only *once*?


### 2. Observations
#### Before We Start Searching
There are a few base cases and trivial things we can rule out before searching:
1. If an element of `L` is 0 or greater than `p` we can ignore it for our purposes.
2. If there is an element in `L` that's equal to `p` it is a valid solution but it might not be the only one.
3. If `p` is 0 and we followed 1. then `p` is a sum of 0 elements of `L`.
4. If `p` equals the total sum of `L` it is a sum of all elements of `L`.


#### The Scope
To be sure that there is no/a solution we ant to try every possible sum of addends of `L`. Only then the search will be thorough.


#### Redundant Work
We want to minimize redundant searches while still keeping the search thorough.
- For starters we know that addition is commutative thus we shouldn't be searching sums like `2 + 4 + 5` and `4 + 5 + 2`. That leaves the question of how to structure the search so that it can be thorough but not redundant in this sense.
- There are also some intuitive things a brute force search would ignore e.g. if `p = 421.24` and we are testing all sums that include the element `350` it wouldn't make intuitive sense to try any element of `L` that is greater than 100. We would also know that any element below 70 would need at least 1 additional addend to sum to `p`.


### 3. Approaches
#### Categorisation
To tackle the 'unintuitiveness' of a brute force search we can create categories for our numbers based on `p`:
If we divide `p` by a resolution factor `r` we get `r` categories to sort the elements of `L` into. Let `i` be the index of a category starting with `i = r` and counting down to `1` for any subsequent categories. *(I will be reversing the category labels for a reason you'll see soon)*
Each category contains all elements of `L` that are equal or less than `i * (p / r)`. In that sense they act like rough percentiles.

**Example:** `p = 421.24` and `r = 5`
In this case `category 5` would contain every element of `L` `<= 84.248`, for `category 4` every element `<= 105.31` and so on...
The last category, `category 1` would contain every element `<= 421.24`.

To make these categories more usable every higher category will not contain any element already included in a lower category e.g. `category 1` wouldn't include `45.89` since it is already included in `category 5`.

Now we get something like:
```
45.87
67.88
67.96
67.02
69.69
40.7
30.45
45.89
------- category 5: 84.248
100.37
------- category 4: 105.31
128.89
140.25
------- category 3: 140.41333333333333
200.74
------- category 2: 210.62
------- category 1: 421.24
```

This has some really useful observations:
Now all elements of a given category have the property that you'll need to sum at least `i` elements of that category to equal `p`. Similarly you will always sum to something `> p` if you add `i + 1` elements of a given category. **Notice how this doesn't work for category 5, the smallest category.**


[tut-tbl]: ./res/tutorial-table.png
[tut-win]: ./res/tutorial-window.png
