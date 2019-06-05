from watson_developer_cloud import DiscoveryV1, WatsonApiException

class WDSWrapper():
    """
    Wrapper class for Watson Discovery Service (WDS).

    This class wraps up many of the common WDS APIs in more convenient packaging. It includes
    functionality for managing configurations, documents and querys.

    Attributes:
        collection_id: A string representing the ID of the collection of interest
    """
    
    def __init__(self, credentials):
        """
        Load credentials and instantiate Discovery object.

        Args:
            credentials: Dictionary containing details for the WDS collection, namely API key
                ('iam_apikey'), URL ('url'), API version ('version'), environment ID
                ('environment_id') and collection ID ('collection_id').
        
        Raises:
            KeyError: Raised if credentials does not contain all of the correct keys.
        """
        try:
            # Discovery object
            self._instance = DiscoveryV1(
                iam_apikey=credentials['iam_apikey'],
                url=credentials['url'],
                version=credentials['version'])

            # Collection details
            self._environment_id = credentials['environment_id']
            self.collection_id = credentials['collection_id']
        except KeyError as e:
            raise KeyError("Argument 'credentials' is missing the following key: " + str(e))
    
    #------------------#
    # Query management #
    # -----------------#

    def query(self, query=None, filter=None, natural_language_query=None, passages=False, description='no description provided', aggregation=None, max_docs=1000, suppress_output=False, return_fields=None):
        """
        Query of a given Discovery collection.
        
        Args:
            query: String defining WDS query to execute.
            filter: String defining the WDS query to apply as a filter to the results.
            description: Description of query (string, for printing).
            aggregation: String defining any WDS aggregations to apply.
            max_docs: Maximum number of documents to return (int).
            field: String specifying which field in the results object to return, e.g. "results", "aggregations"
            suppress_output: Boolean indicating whether to print output. Defaults to False (i.e. 
                prints output).
            return_fields: List of the portions of the document hierarchy to return in results.

        Returns:
            A dictionary ...
        
        Raises:
            WDSCallError: Raised if the API call to WDS produces an error.
        
        TODO add more exceptions, explain return object more
        """
        try:
            results = self._instance.query(
                environment_id=self._environment_id,
                collection_id=self.collection_id,
                query=query,
                filter=filter,
                return_fields=return_fields,
                aggregation=aggregation,
                count=max_docs).get_result()
        except WatsonApiException as e:
            raise WDSCallError(e)
        
        if suppress_output == False:
            print("{:d} documents found for query: {:s}".format(len(results['results']), description))
            if len(results) == max_docs:
                print('Warning: maximum number of documents returned. Results may be incomplete.')
        
        return results
        
#------------#
# Exceptions #
#------------#

class WDSWrapperError(Exception):
    """General Discovery Wrapper error."""
    pass

class WDSCallError(WDSWrapperError):
    """Error for when a Discovery API call fails."""
    pass
