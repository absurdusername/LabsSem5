- ["Quickstart: DataFrame"](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html) -- one page guide by the official docs

- [`pyspark.sql.functions`](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html) -- discover useful column-wise functions here

Always start by creating a so-called "SparkSession"
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
```

To create a Spark DataFrame
```python
df = spark.createDataFrame([
    [1, 10.0, 'asdf'],   # a row`
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

Columns
```python
from pyspark.sql.functions import upper, lower, max, min, avg

df.select(max(df.x)).show()
df.select(upper(df.s)).show() # select upper(s) from df

df.where(df.x == 1).show() # shows matching rows, where() aliases filter()
df.where('x = 1').show() # SQL conditionals are allowed

df.withColumn("upper_s", upper(df.s)).show() # returns df + upper(s)
df.withColumn("x squared", pow(df.x, 2)).show()

fruits.groupBy(fruits.color).count().show()

df.drop(*colnames)
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
df.write.csv(file_path, header=True, mode='overwrite')
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

Handling categorical data (Strings)
```python
indexer = StringIndexer(inputCol='fruit', outputCol='fruit_index')
df = indexer.fit(df).transform(df)
```

Should the need arise to handle numeric categorical data

`StringIndexer -> VectorAssembler -> VectorIndexer`