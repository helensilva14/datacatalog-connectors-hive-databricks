#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import sys

from google.datacatalog_connectors.hive_databricks.sync import datacatalog_synchronizer

__PROJECT_ID = "<PROJECT_ID>"
__LOCATION = "<REGION>"
__HOST = "<IP_HOST>"
__DB_NAME ="<DATABASE_NAME>"
__HMS_USR = "<USER>"
__HMS_PWD = "<PASSWORD>"

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)


datacatalog_synchronizer.DataCatalogSynchronizer(
    project_id=__PROJECT_ID,
    location_id=__LOCATION,
    hive_metastore_db_host=__HOST,
    hive_metastore_db_user=__HMS_USR,
    hive_metastore_db_pass=__HMS_PWD,
    hive_metastore_db_name=__DB_NAME,
    hive_metastore_db_type='mysql').run()