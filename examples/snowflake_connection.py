#!/usr/bin/env python
# coding: utf-8

# Import packages
from all_import import *


def snowflake_connection(user_role = 'BA_CUSTOMERSUCCESS'):
    # Update user_id
    user_id = 'pegah.pooya@genesys.com'
    ctx = snowflake.connector.connect(
    user=user_id,
    role = user_role,
    account='genesysinc', authenticator='externalbrowser')    
    return ctx

