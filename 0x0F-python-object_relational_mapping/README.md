Object Relational Mapping (ORM)
This is a programming technique that links the ueage of python to dtabase management.
Most programs run on some sorr of database management system and it is imperative that
there is a direct link and relation to these database based on the environment in usage.
 The python environment would be use in this code. Which requires that we install the venv
python environment. In thios environment, all depencies(Libraries, modules, packages or databases) 
would remain in a directory only limited to the virtual python environment. This 
would help to skew project-based dependencies to a particular environment without affecting
the system's python environment. The venv is important because it protects the pc's python environment from
any misharp that might happen in the course of running the project. 

The need for ORM is clearly seen and validated. its usage is justified. it has made working with python and SQL
very easy. Such ORM systems are Alchemy and Django's. In ORM, classes becomes tables and instances of 
those classes become rows in a database. How cool is that!!!

The Engine
The engine is the mechanism that establishes a link between your python code and then your database.
Since ORM is basically python or any other object-oriented, ie,. object, code and databses,.ie Relational, 
the engine is very key.You first need to import the create_engine() function from the SQL Alchemy library
and then give it the URL to your database.

The Session
The session function is also needed to create an instance of the current python-database operation.
Inorder to run multiple or single commands to affect a database, the session is needed. The session is 
created using a bind of the engine. Remeber the ngine is the link between the python and the db.
The session is creted with "sessionmaker(bind=engine)" and the result when assigned to a vraiable, 
becomes like a constructer. It is this variable (which is an instance of the class sessionmaker) that
is used t create the individual session. So the first return of sessionmaker is not used to perform
CRUD operations but rather the instances of that. 


Ceating a table
In order to create a table, you need to define a pythonic class that takes attributes that you would 
want your database to hold. You need to give it a __tablename__ and other colum names with values.
So every instance of the class you create would have a different table with different properties.
In creating a table, a sessiopn is noit needed. Base.metadata.create_all(engine) is how to. 

STEPS
1. Design the c=table structure by defininng or creating your class
2. Crete the engine
3. Create the table
4. Create a session
5. Perform your operations

