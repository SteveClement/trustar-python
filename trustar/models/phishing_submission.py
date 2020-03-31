# python 2 backwards compatibility
from __future__ import print_function
from builtins import object, super
from future import standard_library
from six import string_types

# package imports
from ..utils import normalize_timestamp
from .base import ModelBase
from .enum import *


class PhishingSubmission(ModelBase):
    """
    Models a |PhishingSubmission_resource|

    :ivar submission_id: The guid of the email submission
    :ivar title: The title of the email submission (email subject)
    :ivar normalized_triage_score: The score of the email submission
    :ivar context: A list containing dicts which represent IOCs, sources, and scores
                    that contributed to to the triage score.
    """

    def __init__(self,
                 submission_id=None,
                 title=None,
                 normalized_triage_score=None,
                 context=None,
                 response_metadata=None):
        """
        Constructs a PhishingSubmission object.

        """
        self.submission_id = submission_id
        self.title = title
        self.normalized_triage_score = normalized_triage_score
        self.context = context
        self.response_metadata = response_metadata

    @classmethod
    def from_dict(cls, phishing_submission):
        """
        Creates a phishing submission object from a dictionary.

        :param phishing_submission: The phishing submission dictionary.
        :return: The PhishingSubmission object.
        """

        context = phishing_submission.get('context')
        if context is not None:
            context = [PhishingIndicator.from_dict(entity) for entity in context]

        return PhishingSubmission(submission_id=phishing_submission.get('submissionId'),
                                  title=phishing_submission.get('title'),
                                  normalized_triage_score=phishing_submission.get('normalizedTriageScore'),
                                  context=context,
                                  response_metadata=phishing_submission.get('responseMetadata'))

    def to_dict(self, remove_nones=False):
        """
        Creates a dictionary representation of a phishing submission.

        :param remove_nones: Whether ``None`` values should be filtered out of the dictionary.  Defaults to ``False``.
        :return: A PhishingSubmission object.
        """

        if remove_nones:
            return super().to_dict(remove_nones=True)

        phishing_submission_dict = {
            'submissionId': self.submission_id,
            'title': self.title,
            'normalizedTriageScore': self.normalized_triage_score,
            'context': self.context,
            'responseMetadata': self.response_metadata
        }

        return phishing_submission_dict


class PhishingIndicator(ModelBase):
    """
    Models a |PhishingIndicator_resource|.

    :ivar indicator_type: The type of the extracted entity (e.g. URL, IP, ...)
    :ivar value: The value of an extracted entity (e.g. www.badsite.com, etc.)
    :ivar source_key: A string that is associated with the closed source providing context
                       (e.g. 'virustotal', 'crowdstrike_indicator')
    :ivar normalized_source_score: The normalized score associated with a context entity
    """

    def __init__(self,
                 indicator_type=None,
                 value=None,
                 source_key=None,
                 normalized_source_score=None,
                 response_metadata=None):
        """
        Constructs a PhishingIndicator object.
        """
        self.indicator_type = indicator_type
        self.value = value
        self.source_key = source_key
        self.normalized_source_score = normalized_source_score
        self.response_metadata = response_metadata

    @classmethod
    def from_dict(cls, phishing_indicator):
        """
        Creates a phishing indicator object from a dictionary.

        :param phishing_indicator: The phishing indicator dictionary.
        """

        return PhishingIndicator(indicator_type=phishing_indicator.get('indicatorType'),
                                 value=phishing_indicator.get('value'),
                                 source_key=phishing_indicator.get('sourceKey'),
                                 normalized_source_score=phishing_indicator.get('normalizedSourceScore'),
                                 response_metadata=phishing_indicator.get('responseMetadata'))

    def to_dict(self, remove_nones=False):
        """
        Creates a dictionary representation of a phishing indicator.

        :param remove_nones: Whether ``None`` values should be filtered out of the dictionary.  Defaults to ``False``.
        :return: A PhishingIndicator object.
        """

        if remove_nones:
            return super().to_dict(remove_nones=True)

        phishing_indicator_dict = {
            'indicatorType': self.indicator_type,
            'value': self.value,
            'sourceKey': self.source_key,
            'normalizedSourceScore': self.normalized_source_score,
            'responseMetadata': self.response_metadata
        }

        return phishing_indicator_dict
