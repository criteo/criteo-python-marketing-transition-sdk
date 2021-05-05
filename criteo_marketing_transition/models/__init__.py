# coding: utf-8

# flake8: noqa
"""
    Criteo API Transition Swagger

    This is used to help Criteo clients transition from MAPI to Criteo API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from criteo_marketing_transition.models.ad_set_delivery_limitations import AdSetDeliveryLimitations
from criteo_marketing_transition.models.ad_set_frequency_capping import AdSetFrequencyCapping
from criteo_marketing_transition.models.ad_set_geo_location import AdSetGeoLocation
from criteo_marketing_transition.models.ad_set_search_filter import AdSetSearchFilter
from criteo_marketing_transition.models.ad_set_targeting import AdSetTargeting
from criteo_marketing_transition.models.ad_set_targeting_rule import AdSetTargetingRule
from criteo_marketing_transition.models.audience import Audience
from criteo_marketing_transition.models.audience_attributes import AudienceAttributes
from criteo_marketing_transition.models.audience_error import AudienceError
from criteo_marketing_transition.models.audience_name_description import AudienceNameDescription
from criteo_marketing_transition.models.audience_warning import AudienceWarning
from criteo_marketing_transition.models.basic_audience_definition import BasicAudienceDefinition
from criteo_marketing_transition.models.bid_message import BidMessage
from criteo_marketing_transition.models.campaign_bid_change_request import CampaignBidChangeRequest
from criteo_marketing_transition.models.campaign_bid_change_response import CampaignBidChangeResponse
from criteo_marketing_transition.models.campaign_bid_change_response_message_with_details import CampaignBidChangeResponseMessageWithDetails
from criteo_marketing_transition.models.campaign_bid_message import CampaignBidMessage
from criteo_marketing_transition.models.campaign_message import CampaignMessage
from criteo_marketing_transition.models.category_bid_change_request import CategoryBidChangeRequest
from criteo_marketing_transition.models.category_bid_message import CategoryBidMessage
from criteo_marketing_transition.models.category_message import CategoryMessage
from criteo_marketing_transition.models.category_update_error import CategoryUpdateError
from criteo_marketing_transition.models.category_update_input import CategoryUpdateInput
from criteo_marketing_transition.models.category_updates_per_catalog import CategoryUpdatesPerCatalog
from criteo_marketing_transition.models.category_updates_per_catalog_error import CategoryUpdatesPerCatalogError
from criteo_marketing_transition.models.category_updates_per_catalog_error_message_with_details import CategoryUpdatesPerCatalogErrorMessageWithDetails
from criteo_marketing_transition.models.contactlist_amendment import ContactlistAmendment
from criteo_marketing_transition.models.contactlist_amendment_attributes import ContactlistAmendmentAttributes
from criteo_marketing_transition.models.contactlist_amendment_request import ContactlistAmendmentRequest
from criteo_marketing_transition.models.contactlist_operation import ContactlistOperation
from criteo_marketing_transition.models.contactlist_operation_attributes import ContactlistOperationAttributes
from criteo_marketing_transition.models.criteo_api_data_of_portfolio_message import CriteoApiDataOfPortfolioMessage
from criteo_marketing_transition.models.criteo_api_error import CriteoApiError
from criteo_marketing_transition.models.criteo_api_warning import CriteoApiWarning
from criteo_marketing_transition.models.delete_audience_contact_list_response import DeleteAudienceContactListResponse
from criteo_marketing_transition.models.delete_audience_response import DeleteAudienceResponse
from criteo_marketing_transition.models.error_code_response import ErrorCodeResponse
from criteo_marketing_transition.models.error_message import ErrorMessage
from criteo_marketing_transition.models.get_audiences_response import GetAudiencesResponse
from criteo_marketing_transition.models.get_portfolio_response import GetPortfolioResponse
from criteo_marketing_transition.models.inline_object import InlineObject
from criteo_marketing_transition.models.jwt_model import JwtModel
from criteo_marketing_transition.models.modify_audience_response import ModifyAudienceResponse
from criteo_marketing_transition.models.new_audience import NewAudience
from criteo_marketing_transition.models.new_audience_attributes import NewAudienceAttributes
from criteo_marketing_transition.models.new_audience_request import NewAudienceRequest
from criteo_marketing_transition.models.new_audience_response import NewAudienceResponse
from criteo_marketing_transition.models.nillable_ad_set_targeting_rule import NillableAdSetTargetingRule
from criteo_marketing_transition.models.nillable_date_time import NillableDateTime
from criteo_marketing_transition.models.nillable_decimal import NillableDecimal
from criteo_marketing_transition.models.o_auth2_error import OAuth2Error
from criteo_marketing_transition.models.patch_ad_set import PatchAdSet
from criteo_marketing_transition.models.patch_ad_set_bidding import PatchAdSetBidding
from criteo_marketing_transition.models.patch_ad_set_budget import PatchAdSetBudget
from criteo_marketing_transition.models.patch_ad_set_scheduling import PatchAdSetScheduling
from criteo_marketing_transition.models.portfolio_message import PortfolioMessage
from criteo_marketing_transition.models.problem_details import ProblemDetails
from criteo_marketing_transition.models.read_ad_set import ReadAdSet
from criteo_marketing_transition.models.read_ad_set_bidding import ReadAdSetBidding
from criteo_marketing_transition.models.read_ad_set_budget import ReadAdSetBudget
from criteo_marketing_transition.models.read_ad_set_schedule import ReadAdSetSchedule
from criteo_marketing_transition.models.read_model_ad_set_id import ReadModelAdSetId
from criteo_marketing_transition.models.read_model_read_ad_set import ReadModelReadAdSet
from criteo_marketing_transition.models.replace_audience import ReplaceAudience
from criteo_marketing_transition.models.replace_audience_request import ReplaceAudienceRequest
from criteo_marketing_transition.models.replace_audience_response import ReplaceAudienceResponse
from criteo_marketing_transition.models.request_ad_set_search import RequestAdSetSearch
from criteo_marketing_transition.models.requests_ad_set_id import RequestsAdSetId
from criteo_marketing_transition.models.requests_patch_ad_set import RequestsPatchAdSet
from criteo_marketing_transition.models.response_ad_set_id import ResponseAdSetId
from criteo_marketing_transition.models.response_read_ad_set import ResponseReadAdSet
from criteo_marketing_transition.models.responses_ad_set_id import ResponsesAdSetId
from criteo_marketing_transition.models.statistics_report_query_message import StatisticsReportQueryMessage
from criteo_marketing_transition.models.transactions_report_query_data_message import TransactionsReportQueryDataMessage
from criteo_marketing_transition.models.transactions_report_query_entity_message import TransactionsReportQueryEntityMessage
from criteo_marketing_transition.models.transactions_report_query_message import TransactionsReportQueryMessage
from criteo_marketing_transition.models.write_model_ad_set_id import WriteModelAdSetId
from criteo_marketing_transition.models.write_model_patch_ad_set import WriteModelPatchAdSet
