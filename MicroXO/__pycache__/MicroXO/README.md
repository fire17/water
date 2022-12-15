# MicroXO Super Micro Services
General Purpose Micro Service Comunications


For Specific Feature Documentation,
Take a look at [Services](), each with it's own Readme

## General Usages & Examples

To access a known service, simply use: (gps for example)
```
import microxo as xo
print(xo.gps.location)
```

To add a new service, simply use:
```
#foo.py

import microxo as xo
foo = xo.register()

@xo.api
def bar(data=1, auth=None, **kwargs): 
	''' This function will be accessible for other services '''
	# time.sleep(1) # this function runs async, and will return to proper request origin
	return data*data
```

Now you can use it (in any other service)
```
import microxo as xo
print(xo.foo.bar(99)) # prints 9801
```

### Use Data Pub/Sub
Publish as a service:
```
#dataMover.py

import microxo as xo
dataMover = xo.register()

@xo.api
def foo(data=1, auth=None, **kwargs): 
	''' This function will be accessible for other services '''
	ret = data * data
	
	''' Setting data in dataMover service will PUSH data to all subscribed services '''
	
	# Pushing data to all dataMover.foo.bar subscribers
	dataMover.foo.bar = ret
	
	return ret
```
Subscribe to changes:
```
#dataListner.py
import microxo as xo

# Subscribing to foo.res Changes in dataMover Service
xo.dataMover.foo.bar @= lambda data : print( f"Foo was called and returned {data}" )

while(true):
	sleep(1)
```

### Requires:
- Zeroless
- xoDAL

