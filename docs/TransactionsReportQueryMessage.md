# TransactionsReportQueryMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_ids** | **str** | The comma-separated list of advertiser ids. If empty, all the advertisers in the portfolio will be used | [optional] 
**event_type** | **str** | Apply a filter on Event type . | [optional] 
**currency** | **str** | The currency used for the report. ISO 4217 code (three-letter capitals). | 
**format** | **str** | The file format of the generated report: csv, xml, excel or json. | 
**timezone** | **str** | The timezone used for the report. Timezone Database format (Tz). | [optional] [default to 'UTC']
**start_date** | **datetime** | Start date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 
**end_date** | **datetime** | End date of the report. Date component of ISO 8061 format, any time or timezone component is ignored. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


