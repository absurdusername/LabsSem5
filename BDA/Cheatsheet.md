
Always start by creating a so-called "SparkSession"
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
```

To create a Spark DataFrame
```python
df = spark.createDataFrame([
    [1, 10.0, 'asdf'],   # a row
    [2, 20.0, 'qwerty']  # another row
], schema='x int, y float, s string')

df.toPandas() # for desperate times
```

Show the DataFrame
```python
df.show(10) # show the first n rows, df.show() defaults to 20 rows
df.select("x", "y").show() # show selected columns
df.describe("x", "y").show() # summary statistics, or use df.describe().show()
df.printSchema() # DataFrame schema  
```

Showing columns
```python
from pyspark.sql.functions import upper

df.where(df.x == 1).show() # shows matching rows, where() aliases filter()
df.where('x = 1').show() # SQL conditionals are allowed

df.select(upper(df.s)).show() # select upper(s) from df
df.withColumn("upper_s", upper(df.s)).show() # returns df + upper(s)

fruits.groupBy(fruits.color).count().show()
```

UDFs
```python
from pyspark.sql.functions import udf

@udf
def foo(x):
    return 2 * x + 5

df.select(foo(df.x)).show() # usage
```

Reading and writing DataFrames
```python
df.write.csv('foo.csv', header=True)
spark.read.csv('foo.csv', header=True).show()
```

SQL
```python
df.createOrReplaceTempView("foo_table")
spark.sql('''
    select count(*) 
    from foo_table
''')
```