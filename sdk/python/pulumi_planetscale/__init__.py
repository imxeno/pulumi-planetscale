# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .backup import *
from .branch import *
from .database import *
from .get_backup import *
from .get_backups import *
from .get_branch import *
from .get_branch_schema import *
from .get_branch_schema_lint import *
from .get_branches import *
from .get_database import *
from .get_database_read_only_regions import *
from .get_database_regions import *
from .get_databases import *
from .get_oauth_applications import *
from .get_organization import *
from .get_organization_regions import *
from .get_organizations import *
from .get_password import *
from .get_passwords import *
from .get_user import *
from .password import *
from .provider import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_planetscale.config as __config
    config = __config
    import pulumi_planetscale.region as __region
    region = __region
else:
    config = _utilities.lazy_import('pulumi_planetscale.config')
    region = _utilities.lazy_import('pulumi_planetscale.region')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "planetscale",
  "mod": "index/backup",
  "fqn": "pulumi_planetscale",
  "classes": {
   "planetscale:index/backup:Backup": "Backup"
  }
 },
 {
  "pkg": "planetscale",
  "mod": "index/branch",
  "fqn": "pulumi_planetscale",
  "classes": {
   "planetscale:index/branch:Branch": "Branch"
  }
 },
 {
  "pkg": "planetscale",
  "mod": "index/database",
  "fqn": "pulumi_planetscale",
  "classes": {
   "planetscale:index/database:Database": "Database"
  }
 },
 {
  "pkg": "planetscale",
  "mod": "index/password",
  "fqn": "pulumi_planetscale",
  "classes": {
   "planetscale:index/password:Password": "Password"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "planetscale",
  "token": "pulumi:providers:planetscale",
  "fqn": "pulumi_planetscale",
  "class": "Provider"
 }
]
"""
)
