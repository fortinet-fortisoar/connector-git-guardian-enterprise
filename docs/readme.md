## About the connector
GitGuardian Enterprise is a security platform designed to detect, monitor, and remediate secrets (like API keys, passwords, and tokens) and sensitive data exposed in source code, CI/CD pipelines, containers, and developer environments.
<p>This document provides information about the GitGuardian Enterprise Connector, which facilitates automated interactions, with a GitGuardian Enterprise server using FortiSOAR&trade; playbooks. Add the GitGuardian Enterprise Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with GitGuardian Enterprise.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-git-guardian-enterprise`

## Prerequisites to configuring the connector
- You must have the URL of GitGuardian Enterprise server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the GitGuardian Enterprise server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>GitGuardian Enterprise</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the server URL of the GitGuardian Enterprise server to connect and perform automated operations.<br>
<tr><td>API Key<br></td><td>Specify the API Key to connect to the endpoint and perform automated operations.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get All Audit Logs<br></td><td>Retrieve a list of audit logs from the GitGuardian Enterprise server using the specified filter parameters.<br></td><td>get_all_audit_logs <br/>Investigation<br></td></tr>
<tr><td>Get Audit Log Details<br></td><td>Retrieve specific audit log details from the GitGuardian Enterprise server using the provided audit log ID.<br></td><td>get_audit_log_details <br/>Investigation<br></td></tr>
<tr><td>Get Audit Log Actors/Types<br></td><td>Retrieve a list of audit log actors or types from the GitGuardian Enterprise server based on the audit log metadata and other filter parameter you have specified.<br></td><td>get_audit_log_actors_types <br/>Investigation<br></td></tr>
<tr><td>Get All Git Users<br></td><td>Retrieve a list of git users from the GitGuardian Enterprise server based on the git type and other filter parameters you have specified.<br></td><td>get_all_git_users <br/>Investigation<br></td></tr>
<tr><td>Get Git User Details<br></td><td>Retrieve specific git user details from the GitGuardian Enterprise server based on the git type and it's ID specified.<br></td><td>get_git_user_details <br/>Investigation<br></td></tr>
<tr><td>Create Keyword<br></td><td>Creates a new keyword in the GitGuardian Enterprise server, it will be in PENDING state until GitGuardian approves or refuses the keyword.<br></td><td>create_keyword <br/>Investigation<br></td></tr>
<tr><td>Get All Keywords<br></td><td>Retrieve a list of keywords from the GitGuardian Enterprise server using the specified filter parameters.<br></td><td>get_all_keywords <br/>Investigation<br></td></tr>
<tr><td>Get Keyword Details<br></td><td>Retrieve specific keyword details from the GitGuardian Enterprise server based on the keyword type and it's ID specified.<br></td><td>get_keyword_details <br/>Investigation<br></td></tr>
<tr><td>Update Keyword Details<br></td><td>Update a specific keyword details in the GitGuardian Enterprise server based on the keyword type, name, labels, and it's ID specified.<br></td><td>update_keyword_details <br/>Investigation<br></td></tr>
<tr><td>Delete Keyword<br></td><td>Deletes a specific keyword from the GitGuardian Enterprise server based on the keyword type and it's ID specified.<br></td><td>delete_keyword <br/>Investigation<br></td></tr>
<tr><td>Export Keywords<br></td><td>Exports the keyword as CSV file from the GitGuardian Enterprise server.<br></td><td>export_keywords <br/>Investigation<br></td></tr>
<tr><td>Get All Incident Secrets<br></td><td>Retrieve a list of incident secrets from the GitGuardian Enterprise server using the specified filter parameters.<br></td><td>get_all_incident_secrets <br/>Investigation<br></td></tr>
<tr><td>Get Incident Secret Details<br></td><td>Retrieve specific incident secret details from the GitGuardian Enterprise server using the provided incident secret ID.<br></td><td>get_incident_secret_details <br/>Investigation<br></td></tr>
<tr><td>Update Incident Secret Status<br></td><td>Updates a specific incident secret details in the GitGuardian Enterprise server using the provided incident secret ID and status.<br></td><td>update_incident_secret_status <br/>Investigation<br></td></tr>
<tr><td>Create Incident Secret Shared Link<br></td><td>Create a public link for the incident to request feedback from anyone outside of the platform using the provided incident secret ID.<br></td><td>create_incident_secret_shared_link <br/>Investigation<br></td></tr>
<tr><td>Rotate Incident Secret Shared Link<br></td><td>Delete any of the previously created links, and create a fresh one using the provided incident secret ID.<br></td><td>rotate_incident_secret_shared_link <br/>Investigation<br></td></tr>
<tr><td>Delete Incident Secret Shared Link<br></td><td>Deactivate and delete a given shared link using the provided incident secret ID.<br></td><td>delete_incident_secret_shared_link <br/>Investigation<br></td></tr>
<tr><td>Get All Incident Keywords<br></td><td>Retrieve a list of incident keywords from the GitGuardian Enterprise server using the specified filter parameters.<br></td><td>get_all_incident_keywords <br/>Investigation<br></td></tr>
<tr><td>Get Incident Keyword Details<br></td><td>Retrieve specific incident keyword details from the GitGuardian Enterprise server based on the incident keyword ID specified.<br></td><td>get_incident_keyword_details <br/>Investigation<br></td></tr>
<tr><td>Update Incident Keyword Status<br></td><td>Updates a specific incident keyword details in the GitGuardian Enterprise server using the provided incident keyword ID and status.<br></td><td>update_incident_keyword_status <br/>Investigation<br></td></tr>
<tr><td>Get Incident Secret Note<br></td><td>Retrieve specific incident secret note from the GitGuardian Enterprise server using the provided incident secret ID.<br></td><td>get_incident_secret_note <br/>Investigation<br></td></tr>
<tr><td>Get Incident Keyword Note<br></td><td>Retrieve specific incident keyword note from the GitGuardian Enterprise server based on the incident keyword ID specified.<br></td><td>get_incident_keyword_note <br/>Investigation<br></td></tr>
<tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>execute_an_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get All Audit Logs
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Include Actor(s)<br></td><td>Filter results to include only logs performed by specific actor usernames.<br>
</td></tr><tr><td>Exclude Actor(s)<br></td><td>Exclude audit logs performed by specified actor usernames.<br>
</td></tr><tr><td>Actor Email<br></td><td>Filter logs based on the email address of the actor who performed the action.<br>
</td></tr><tr><td>Ordering<br></td><td>Specify how results should be ordered, such as by timestamp or actor name.<br>
</td></tr><tr><td>Full-Text Search<br></td><td>Full-text search across multiple fields of the audit logs.<br>
</td></tr><tr><td>Type<br></td><td>Filter audit logs by a specific event type.<br>
</td></tr><tr><td>Include Types<br></td><td>Include logs of multiple event types.<br>
</td></tr><tr><td>Exclude Types<br></td><td>Exclude logs of specific event types.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve audit log results when pagination is used. Default is 0.<br>
</td></tr><tr><td>Results Per Page<br></td><td>Number of results to return per page when pagination is applied.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Audit Log Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Audit Log ID<br></td><td>Specify the audit log ID to retrieve its details from the GitGuardian Enterprise server. You can obtain the Audit Log ID from the response of the "Get All Audit Logs" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Audit Log Actors/Types
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Audit Log Metadata<br></td><td>Select the audit log metadata to retrieve its details from the GitGuardian Enterprise server. "Audit Log Actors" retrieve a list of members whose actions have generated audit log entries. "Audit Log Types" retrieve a list of available audit log types.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve audit log actors/types results when pagination is used. Default is 0.<br>
</td></tr><tr><td>Results Per Page<br></td><td>Number of results to return per page when pagination is applied.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Git Users
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Git Type<br></td><td>Select the type of Git platform to retrieve a users. You can choose from the following options: GIT Users or GITHub Users.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve git users results when pagination is used. Default is 0.<br>
</td></tr><tr><td>Results Per Page<br></td><td>Number of results to return per page when pagination is applied.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Git User Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Git Type<br></td><td>Select the type of Git platform to retrieve a users. You can choose from the following options: GIT Users or GITHub Users.<br>
<strong>If you choose 'GIT Users'</strong><ul><li>GIT User ID: Specify the GIT user ID to retrieve its details from the GitGuardian Enterprise server. You can obtain the GIT User ID from the response of the "Get All Git Users" action.</li></ul><strong>If you choose 'GITHub Users'</strong><ul><li>GITHub User ID: Specify the GITHub user ID to retrieve its details from the GitGuardian Enterprise server. You can obtain the GITHub User ID from the response of the "Get All Git Users" action.</li></ul></td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Keyword
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Keyword ID<br></td><td>Specify the keyword ID based on which you want to create a keyword.<br>
</td></tr><tr><td>Keyword Name<br></td><td>Specify the keyword name based on which you want to create a keyword.<br>
</td></tr><tr><td>Keyword<br></td><td>Specify the keyword based on which you want to create a keyword.<br>
</td></tr><tr><td>Categories<br></td><td>Select one or more options of categories based on which you want to create a keyword. You can choose one or more from the following options: Secret Grasper, Incident Raiser, or Incident Raiser On Perimeter.<br>
</td></tr><tr><td>Status<br></td><td>Select the status based on which you want to create a keyword. You can choose from the following options: Pending, Active, or Deactivated.<br>
</td></tr><tr><td>Keyword Type<br></td><td>Select the type of the keyword based on which you want to create a keyword. You can choose from the following options: Raw or Regexp<br>
</td></tr><tr><td>Labels<br></td><td>Specify the comma-separated list of integer labels based on which you want to create a keyword.<br>
</td></tr><tr><td>Created At<br></td><td>Select a date and time to retrieve results that include only those items that were created after the specified timestamp.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Keywords
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Keyword Type<br></td><td>Select the type of keyword to retrieve a details. You can choose from the following options: Incident Raiser or Secret Grasper.<br>
</td></tr><tr><td>Categories<br></td><td>Select the category based on which you want to retrieve a keywords. You can choose from the following options: Secret Grasper, Incident Raiser, or Incident Raiser On Perimeter.<br>
</td></tr><tr><td>Status<br></td><td>Select the status based on which you want to retrieve a keywords. You can choose from the following options: Pending, Active, or Deactivated.<br>
</td></tr><tr><td>Keyword Type<br></td><td>Select the type of the keyword based on which you want to retrieve a keywords. You can choose from the following options: Raw or Regexp<br>
</td></tr><tr><td>Ordering<br></td><td>Specify how results should be ordered, such as by name or status.<br>
</td></tr><tr><td>Full-Text Search<br></td><td>Full-text search across multiple fields of the keywords.<br>
</td></tr><tr><td>Include Labels<br></td><td>Include keywords of multiple labels.<br>
</td></tr><tr><td>Exclude Labels<br></td><td>Exclude keywords of multiple labels<br>
</td></tr><tr><td>Include Status<br></td><td>Include keywords of multiple status.<br>
</td></tr><tr><td>Exclude Status<br></td><td>Exclude keywords of multiple status<br>
</td></tr><tr><td>Include Types<br></td><td>Include logs of multiple event types.<br>
</td></tr><tr><td>Exclude Types<br></td><td>Exclude logs of multiple event types.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve keywords results when pagination is used. Default is 0.<br>
</td></tr><tr><td>Results Per Page<br></td><td>Number of results to return per page when pagination is applied.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Keyword Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Keyword Type<br></td><td>Select the type of keyword to retrieve a details. You can choose from the following options: Incident Raiser or Secret Grasper.<br>
<strong>If you choose 'Incident Raiser'</strong><ul><li>Incident Raiser ID: Specify the Incident Raiser ID to retrieve its details from the GitGuardian Enterprise server. You can obtain the Incident Raiser ID from the response of the "Get All Keywords" action.</li></ul><strong>If you choose 'Secret Grasper'</strong><ul><li>Secret Grasper ID: Specify the Secret Grasper ID to retrieve its details from the GitGuardian Enterprise server. You can obtain the Secret Grasper ID from the response of the "Get All Keywords" action.</li></ul></td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Update Keyword Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Keyword Type<br></td><td>Select the type of keyword to update a details. You can choose from the following options: Incident Raiser or Secret Grasper.<br>
<strong>If you choose 'Incident Raiser'</strong><ul><li>Incident Raiser ID: Specify the Incident Raiser ID to update its details from the GitGuardian Enterprise server. You can obtain the Incident Raiser ID from the response of the "Get All Keywords" action.</li></ul><strong>If you choose 'Secret Grasper'</strong><ul><li>Secret Grasper ID: Specify the Secret Grasper ID to update its details from the GitGuardian Enterprise server. You can obtain the Secret Grasper ID from the response of the "Get All Keywords" action.</li></ul></td></tr><tr><td>Labels<br></td><td>Specify the comma-separated list of integer labels based on which you want to update a keyword.<br>
</td></tr><tr><td>New Keyword Name<br></td><td>Specify the new name of the keyword based on which you want to update a keyword.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Delete Keyword
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Keyword Type<br></td><td>Select the type of keyword to delete a specific keyword. You can choose from the following options: Incident Raiser or Secret Grasper.<br>
<strong>If you choose 'Incident Raiser'</strong><ul><li>Incident Raiser ID: Specify the Incident Raiser ID to delete its details from the GitGuardian Enterprise server. You can obtain the Incident Raiser ID from the response of the "Get All Keywords" action.</li></ul><strong>If you choose 'Secret Grasper'</strong><ul><li>Secret Grasper ID: Specify the Secret Grasper ID to delete its details from the GitGuardian Enterprise server. You can obtain the Secret Grasper ID from the response of the "Get All Keywords" action.</li></ul></td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Export Keywords
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get All Incident Secrets
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Full-Text Search<br></td><td>Full-text search across multiple fields of the incident secrets.<br>
</td></tr><tr><td>Severity<br></td><td>Specify the comma-separated list of severity based on which you want to retrieve a incident secrets.<br>
</td></tr><tr><td>Status<br></td><td>Specify the comma-separated list of status based on which you want to retrieve a incident secrets.<br>
</td></tr><tr><td>Created At (Current Period)<br></td><td>Select a time range to filter incident secrets based on when they were created. You can choose from the following current Day, Week, Month, or Year.<br>
</td></tr><tr><td>Created From<br></td><td>Select a date and time to retrieve results that include only those items that were created after the specified timestamp.<br>
</td></tr><tr><td>Created To<br></td><td>Select a date and time to retrieve results that include only those items that were created before the specified timestamp.<br>
</td></tr><tr><td>Ordering<br></td><td>Specify how results should be ordered, such as by timestamp or actor name.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve incident keywords results when pagination is used. Default is 0.<br>
</td></tr><tr><td>Results Per Page<br></td><td>Number of results to return per page when pagination is applied.<br>
</td></tr><tr><td>Additional Parameters<br></td><td>Specify additional parameters with which to filter incident secrets in GitGuardian Enterprise server. You can refer this link for more fields: https://enterprise.gitguardian.com/api/docs#operation/incidents_secrets_list<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Incident Secret Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Secret ID<br></td><td>Specify the incident secret ID to retrieve its details from the GitGuardian Enterprise server. You can obtain the Incident Secret ID from the response of the "Get All Incident Secrets" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Update Incident Secret Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Secret ID<br></td><td>Specify the incident secret ID to update its details in the GitGuardian Enterprise server. You can obtain the Incident Secret ID from the response of the "Get All Incident Secrets" action.<br>
</td></tr><tr><td>Status<br></td><td>Select the status based on which you want to update a incident secret. You can choose from the following options: Acknowledge, Add Note, Assign, Reopen, Resolve, Set Severity, UnAcknowledge, or UnAssign.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Incident Secret Shared Link
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Secret ID<br></td><td>Specify the incident secret ID to create shared link in the GitGuardian Enterprise server. You can obtain the Incident Secret ID from the response of the "Get All Incident Secrets" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Rotate Incident Secret Shared Link
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Secret ID<br></td><td>Specify the incident secret ID to rotate shared link in the GitGuardian Enterprise server. You can obtain the Incident Secret ID from the response of the "Get All Incident Secrets" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Delete Incident Secret Shared Link
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Secret ID<br></td><td>Specify the incident secret ID to deactivate and delete shared link in the GitGuardian Enterprise server. You can obtain the Incident Secret ID from the response of the "Get All Incident Secrets" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Incident Keywords
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve incident keywords results when pagination is used. Default is 0.<br>
</td></tr><tr><td>Results Per Page<br></td><td>Number of results to return per page when pagination is applied.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Incident Keyword Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Keyword ID<br></td><td>Specify the Incident Keyword ID to retrieve its details from the GitGuardian Enterprise server. You can obtain the Incident Keyword ID from the response of the "Get All Incident Keywords" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Update Incident Keyword Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Keyword ID<br></td><td>Specify the incident keyword ID to update its details in the GitGuardian Enterprise server. You can obtain the Incident Keyword ID from the response of the "Get All Incident Keywords" action.<br>
</td></tr><tr><td>Status<br></td><td>Select the status based on which you want to update a incident keyword. You can choose from the following options: Acknowledge, Add Note, Assign, Reopen, Resolve, Set Severity, UnAcknowledge, or UnAssign.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Incident Secret Note
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Secret ID<br></td><td>Specify the incident secret ID to retrieve its note details from the GitGuardian Enterprise server. You can obtain the Incident Secret ID from the response of the "Get All Incident Secrets" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Incident Keyword Note
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident Keyword ID<br></td><td>Specify the Incident Keyword ID to retrieve its note details from the GitGuardian Enterprise server. You can obtain the Incident Keyword ID from the response of the "Get All Incident Keywords" action.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options:  

DELETE 

GET 

PATCH 

POST 

PUT <br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be images/pic.jpg.<br>
</td></tr><tr><td>Query Parameters<br></td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - GitGuardian Enterprise - 1.0.0` playbook collection comes bundled with the GitGuardian Enterprise connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the GitGuardian Enterprise connector.

- Create Incident Secret Shared Link
- Create Keyword
- Delete Incident Secret Shared Link
- Delete Keyword
- Execute an API Request
- Export Keywords
- Get All Audit Logs
- Get All Git Users
- Get All Incident Keywords
- Get All Incident Secrets
- Get All Keywords
- Get Audit Log Actors/Types
- Get Audit Log Details
- Get Git User Details
- Get Incident Keyword Details
- Get Incident Keyword Note
- Get Incident Secret Details
- Get Incident Secret Note
- Get Keyword Details
- Rotate Incident Secret Shared Link
- Update Incident Keyword Status
- Update Incident Secret Status
- Update Keyword Details

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
