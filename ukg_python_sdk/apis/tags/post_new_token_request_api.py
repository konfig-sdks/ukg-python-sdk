# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.signin_oauth2_t_tenant_name_access_token.post import ObtainOAuthToken
from ukg_python_sdk.apis.tags.post_new_token_request_api_raw import PostNewTokenRequestApiRaw


class PostNewTokenRequestApi(
    ObtainOAuthToken,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PostNewTokenRequestApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PostNewTokenRequestApiRaw(api_client)
