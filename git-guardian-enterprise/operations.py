"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import requests, json
from connectors.core.connector import get_logger, ConnectorError
from .constants import *

logger = get_logger('git-guardian-enterprise')


class GitGuardianEnterprise(object):

    def __init__(self, config):
        url = config.get('server_url', '').strip('/')
        if not url.startswith('https://') and not url.startswith('http://'):
            self.url = 'https://{0}/api/v1/'.format(url)
        else:
            self.url = url + '/api/v1/'
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl', False)
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + self.api_key
        }

    def make_api_call(self, endpoint, method='GET', payload=None, params=None):
        service_endpoint = self.url + endpoint
        try:
            response = requests.request(method, service_endpoint, json=payload,
                                        headers=self.headers, params=params,
                                        verify=self.verify_ssl)
            if response.ok or response.status_code == 204:
                logger.info('Successfully got response for url {0}'.format(service_endpoint))
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response
            else:
                logger.error("{0}".format(response.status_code))
                raise ConnectorError("{0}:{1}".format(response.status_code, response.text))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError(
                'The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid Credentials')
        except Exception as err:
            raise ConnectorError(str(err))


def check_payload(payload):
    updated_payload = {}
    for key, value in payload.items():
        if isinstance(value, dict):
            nested = check_payload(value)
            if len(nested.keys()) > 0:
                updated_payload[key] = nested
        elif value != '' and value is not None:
            updated_payload[key] = value
    return updated_payload


def get_all_audit_logs(config, params):
    endpoint = "audit_logs"

    def ensure_list(key):
        """Convert comma-separated string to list for a given key in params."""
        value = params.get(key)
        if value:
            params[key] = value if isinstance(value, list) else value.split(",")

    # Normalize relevant keys to lists
    for key in ['actor__in', 'actor__nin', 'actor_email', 'type', 'type__in', 'type__nin']:
        ensure_list(key)

    ge = GitGuardianEnterprise(config)
    query_parameters = check_payload(params)
    return ge.make_api_call(endpoint, params=query_parameters)


def get_audit_log_details(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "audit_logs/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint)


def get_audit_log_actors_types(config, params):
    ge = GitGuardianEnterprise(config)
    audit_log_metadata = params.get('audit_log_metadata')
    if audit_log_metadata == "Audit Log Actors":
        endpoint = "audit_logs/actors"
    else:
        endpoint = "audit_logs/types"
    query_parameters = check_payload(params)
    return ge.make_api_call(endpoint, params=query_parameters)


def get_all_git_users(config, params):
    ge = GitGuardianEnterprise(config)
    git_type = params.get('git_type')
    if git_type == "GIT Users":
        endpoint = "git_users"
    else:
        endpoint = "github_users"
    query_parameters = check_payload(params)
    return ge.make_api_call(endpoint, params=query_parameters)


def get_git_user_details(config, params):
    ge = GitGuardianEnterprise(config)
    git_type = params.get('git_type')
    if git_type == "GIT Users":
        endpoint = "git_users/{0}".format(params.get('id'))
    else:
        endpoint = "github_users/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint)


def create_keyword(config, params):
    ge = GitGuardianEnterprise(config)
    keyword_type = params.get('keyword_type')
    if keyword_type == "Incident Raiser":
        endpoint = "keywords/incident_raisers"
    else:
        endpoint = "keywords/secret_graspers"
    categories = params.get('categories', [])
    labels = params.get('labels')
    payload = {
        "categories": [CATEGORIES.get(category) for category in categories],
        "created_at": params.get('created_at'),
        "id": params.get('id'),
        "keyword": params.get('keyword'),
        "labels": [int(label) for label in labels if str(label).isdigit()],
        "name": params.get('name'),
        "status": params.get('status').lower(),
        "type": params.get('type').lower()
    }
    query_parameters = check_payload(payload)
    return ge.make_api_call(endpoint, method="POST", params=query_parameters)


def get_all_keywords(config, params):
    keyword_type = params.get('keyword_type')
    if keyword_type == "Incident Raiser":
        endpoint = "keywords/incident_raisers"
    else:
        endpoint = "keywords/secret_graspers"
    if params.get('categories'):
        params['categories'] = CATEGORIES.get(params.get('categories'))
    if params.get('status'):
        params['status'] = params.get('status').lower()
    if params.get('type'):
        params['type'] = params.get('type').lower()

    def ensure_list(key):
        """Convert comma-separated string to list for a given key in params."""
        value = params.get(key)
        if value:
            params[key] = value if isinstance(value, list) else value.split(",")

    # Normalize relevant keys to lists
    for key in ['labels__in', 'labels__nin', 'status__in', 'status__nin', 'type__in', 'type__nin']:
        ensure_list(key)

    ge = GitGuardianEnterprise(config)
    query_parameters = check_payload(params)
    return ge.make_api_call(endpoint, params=query_parameters)


def get_keyword_details(config, params):
    ge = GitGuardianEnterprise(config)
    keyword_type = params.get('keyword_type')
    if keyword_type == "Incident Raiser":
        endpoint = "keywords/incident_raisers/{0}".format(params.get('id'))
    else:
        endpoint = "keywords/secret_graspers/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint)


def update_keyword_details(config, params):
    ge = GitGuardianEnterprise(config)
    keyword_type = params.get('keyword_type')
    if keyword_type == "Incident Raiser":
        endpoint = "keywords/incident_raisers/{0}".format(params.pop('id'))
    else:
        endpoint = "keywords/secret_graspers/{0}".format(params.pop('id'))
    labels = params.get('labels')
    if labels:
        params['labels'] = labels if isinstance(labels, list) else [int(x) for x in labels.split(",")]
    query_parameters = check_payload(params)
    return ge.make_api_call(endpoint, method="PATCH", params=query_parameters)


def delete_keyword(config, params):
    ge = GitGuardianEnterprise(config)
    keyword_type = params.get('keyword_type')
    if keyword_type == "Incident Raiser":
        endpoint = "keywords/incident_raisers/{0}".format(params.get('id'))
    else:
        endpoint = "keywords/secret_graspers/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint, method="DELETE")


def export_keywords(config, params):
    ge = GitGuardianEnterprise(config)
    keyword_type = params.get('keyword_type')
    if keyword_type == "Incident Raiser":
        endpoint = "keywords/incident_raisers/export"
    else:
        endpoint = "keywords/secret_graspers/export"
    return ge.make_api_call(endpoint)


def get_all_incident_secrets(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/secrets"
    severity = params.get('severity')
    status = params.get('status')
    payload = {
        "search": params.get('search'),
        "severity": severity if isinstance(severity, list) else severity.split(',') if isinstance(severity,
                                                                                                  str) else '',
        "status": status if isinstance(status, list) else status.split(',') if isinstance(status, str) else '',
        "created_at__current": params.get('created_at__current').lower() if params.get('created_at__current') else '',
        "created_at__from": params.get('created_at__from') if params.get('created_at__from') else '',
        "created_at__to": params.get('created_at__to') if params.get('created_at__to') else '',
        "ordering": params.get('ordering'),
        "page": params.get('page'),
        "per_page": params.get('per_page')
    }
    additional_fields = params.get('additional_fields')
    if additional_fields:
        payload.update(additional_fields)
    query_parameters = check_payload(payload)
    return ge.make_api_call(endpoint, params=query_parameters)


def get_incident_secret_details(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/secrets/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint)


def update_incident_secret_status(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/secrets/{0}/{1}".format(params.get('id'), INCIDENT_ACTION.get(params.get('action')))
    return ge.make_api_call(endpoint, method="POST")


def create_incident_secret_shared_link(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/secrets/{0}/share".format(params.get('id'))
    return ge.make_api_call(endpoint, method="POST")


def rotate_incident_secret_shared_link(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/secrets/{0}/share".format(params.get('id'))
    return ge.make_api_call(endpoint, method="PUT")


def delete_incident_secret_shared_link(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/secrets/{0}/share".format(params.get('id'))
    return ge.make_api_call(endpoint, method="DELETE")


def get_all_incident_keywords(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/keywords"
    query_parameters = check_payload(params)
    return ge.make_api_call(endpoint, params=query_parameters)


def get_incident_keyword_details(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/keywords/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint)


def update_incident_keyword_status(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "incidents/keywords/{0}/{1}".format(params.get('id'), INCIDENT_ACTION.get(params.get('action')))
    return ge.make_api_call(endpoint, method="POST")


def get_incident_secret_note(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "secrets/notes/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint)


def get_incident_keyword_note(config, params):
    ge = GitGuardianEnterprise(config)
    endpoint = "keyword/notes/{0}".format(params.get('id'))
    return ge.make_api_call(endpoint)


def execute_an_api_call(config, params):
    try:
        ge = GitGuardianEnterprise(config)
        endpoint = params.get("endpoint")
        http_method = params.get("method")
        query_params = params.get("query_params") if params.get("query_params") else {}
        payload = params.get("payload") if params.get("payload") else {}
        logger.debug("Payload: {0}".format(payload))
        response = ge.make_api_call(endpoint, method=http_method, params=query_params, payload=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def _check_health(config):
    try:
        ge = GitGuardianEnterprise(config)
        endpoint = "is_alive"
        resp = ge.make_api_call(endpoint)
        if resp:
            return True
    except Exception as err:
        logger.info(str(err))
        raise ConnectorError(str(err))


operations = {
    'get_all_audit_logs': get_all_audit_logs,
    'get_audit_log_details': get_audit_log_details,
    'get_audit_log_actors_types': get_audit_log_actors_types,
    'get_all_git_users': get_all_git_users,
    'get_git_user_details': get_git_user_details,
    'create_keyword': create_keyword,
    'get_all_keywords': get_all_keywords,
    'get_keyword_details': get_keyword_details,
    'update_keyword_details': update_keyword_details,
    'delete_keyword': delete_keyword,
    'export_keywords': export_keywords,
    'get_all_incident_secrets': get_all_incident_secrets,
    'get_incident_secret_details': get_incident_secret_details,
    'update_incident_secret_status': update_incident_secret_status,
    'create_incident_secret_shared_link': create_incident_secret_shared_link,
    'rotate_incident_secret_shared_link': rotate_incident_secret_shared_link,
    'delete_incident_secret_shared_link': delete_incident_secret_shared_link,
    'get_all_incident_keywords': get_all_incident_keywords,
    'get_incident_keyword_details': get_incident_keyword_details,
    'update_incident_keyword_status': update_incident_keyword_status,
    'get_incident_secret_note': get_incident_secret_note,
    'get_incident_keyword_note': get_incident_keyword_note,
    'execute_an_api_call': execute_an_api_call
}
