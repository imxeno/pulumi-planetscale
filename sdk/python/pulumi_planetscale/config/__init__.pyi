# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

accessToken: Optional[str]
"""
Name of the service token to use. Alternatively, use `PLANETSCALE_SERVICE_TOKEN_NAME`. Mutually exclusive with
`service_token_name` and `service_token`.
"""

endpoint: Optional[str]
"""
If set, points the API client to a different endpoint than `https:://api.planetscale.com/v1`.
"""

serviceToken: Optional[str]
"""
Value of the service token to use. Alternatively, use `PLANETSCALE_SERVICE_TOKEN`. Mutually exclusive with
`access_token`.
"""

serviceTokenName: Optional[str]
"""
Name of the service token to use. Alternatively, use `PLANETSCALE_SERVICE_TOKEN_NAME`. Mutually exclusive with
`access_token`.
"""

