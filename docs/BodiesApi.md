# swagger_client.BodiesApi

All URIs are relative to *https://api.le-systeme-solaire.net/rest.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bodies_get**](BodiesApi.md#bodies_get) | **GET** /bodies | List
[**bodies_id_get**](BodiesApi.md#bodies_id_get) | **GET** /bodies/{id} | read


# **bodies_get**
> object bodies_get(data=data, exclude=exclude, order=order, page=page, row_data=row_data, filter=filter, satisfy=satisfy)

List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BodiesApi()
data = 'data_example' # str | The data you want to retrieve (comma separated). Example: id,semimajorAxis,isPlanet. (optional)
exclude = 'exclude_example' # str | One or more data you want to exclude (comma separated). Example: id,isPlanet. (optional)
order = 'order_example' # str | A data you want to sort on and the sort direction (comma separated). Example: id,desc. Only one data is authorized. (optional)
page = 'page_example' # str | Page number (number>=1) and page size (size>=1 and 20 by default) (comma separated). NB: You cannot use \"page\" without \"order\"! Example: 1,10. (optional)
row_data = true # bool | Transform the object in records. NB: This can also be done client-side in JavaScript! (optional)
filter = ['filter_example'] # list[str] | Filters to be applied. Each filter consists of a data, an operator and a value (comma separated). Example: id,eq,mars. Accepted operators are : cs (like) - sw (start with) - ew (end with) - eq (equal) - lt (less than) - le (less or equal than) - ge (greater or equal than) - gt (greater than) - bt (between). And all opposites operators : ncs - nsw - new - neq - nlt - nle - nge - ngt - nbt. Note : if anyone filter is invalid, all filters will be ignore. (optional)
satisfy = 'satisfy_example' # str | Should all filters match (default)? Or any? (optional)

try:
    # List
    api_response = api_instance.bodies_get(data=data, exclude=exclude, order=order, page=page, row_data=row_data, filter=filter, satisfy=satisfy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BodiesApi->bodies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| The data you want to retrieve (comma separated). Example: id,semimajorAxis,isPlanet. | [optional] 
 **exclude** | **str**| One or more data you want to exclude (comma separated). Example: id,isPlanet. | [optional] 
 **order** | **str**| A data you want to sort on and the sort direction (comma separated). Example: id,desc. Only one data is authorized. | [optional] 
 **page** | **str**| Page number (number&gt;&#x3D;1) and page size (size&gt;&#x3D;1 and 20 by default) (comma separated). NB: You cannot use \&quot;page\&quot; without \&quot;order\&quot;! Example: 1,10. | [optional] 
 **row_data** | **bool**| Transform the object in records. NB: This can also be done client-side in JavaScript! | [optional] 
 **filter** | [**list[str]**](str.md)| Filters to be applied. Each filter consists of a data, an operator and a value (comma separated). Example: id,eq,mars. Accepted operators are : cs (like) - sw (start with) - ew (end with) - eq (equal) - lt (less than) - le (less or equal than) - ge (greater or equal than) - gt (greater than) - bt (between). And all opposites operators : ncs - nsw - new - neq - nlt - nle - nge - ngt - nbt. Note : if anyone filter is invalid, all filters will be ignore. | [optional] 
 **satisfy** | **str**| Should all filters match (default)? Or any? | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bodies_id_get**
> object bodies_id_get(id)

read

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BodiesApi()
id = 'id_example' # str | Identifier for item.

try:
    # read
    api_response = api_instance.bodies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BodiesApi->bodies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier for item. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

