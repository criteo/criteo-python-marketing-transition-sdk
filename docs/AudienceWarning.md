# AudienceWarning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** | (REQUIRED) The Correlation ID provided by the Gateway. It is also a unique identifier for this particular occurrence of the problem. | [optional] 
**type** | **str** | (REQUIRED) The classification of the error | 
**code** | **str** | (REQUIRED) A machine-readable unique error code, expressed as a string value. The format used must be kebab-case. | 
**instance** | **str** | (REQUIRED) A URI reference that identifies the specific occurrence of the problem | 
**title** | **str** | (RECOMMENDED) A short, human-readable summary of the problem type | [optional] 
**detail** | **str** | (REQUIRED) A human-readable explanation specific to this occurrence of the problem | 
**source** | [**object**](.md) | (OPTIONAL) A machine-readable structure to reference to the exact location(s) causing the error(s) | [optional] 
**stack_trace** | **list[str]** | (NEVER IN PRODUCTION) A human-readable stacktrace produced by the implementation technology | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


