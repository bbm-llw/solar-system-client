# swagger_client.KnowncountApi

All URIs are relative to *https://api.le-systeme-solaire.net/rest.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**knowncount_get**](KnowncountApi.md#knowncount_get) | **GET** /knowncount | List
[**knowncount_id_get**](KnowncountApi.md#knowncount_id_get) | **GET** /knowncount/{id} | read


# **knowncount_get**
> object knowncount_get(row_data=row_data)

List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KnowncountApi()
row_data = true # bool | Transform the object in records. NB: This can also be done client-side in JavaScript! (optional)

try:
    # List
    api_response = api_instance.knowncount_get(row_data=row_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowncountApi->knowncount_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **row_data** | **bool**| Transform the object in records. NB: This can also be done client-side in JavaScript! | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowncount_id_get**
> object knowncount_id_get(id)

read

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KnowncountApi()
id = 'id_example' # str | Identifier for item.

try:
    # read
    api_response = api_instance.knowncount_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowncountApi->knowncount_id_get: %s\n" % e)
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

