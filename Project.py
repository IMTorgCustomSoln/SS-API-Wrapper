import sys
import timeit
import pandas
import requests


def time_usage(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        retval = func(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print(" -elapsed time: %f" % (elapsed))
        return retval
    return wrapper



class Project(dict):
    """ container for project data """
    # system (class) config
    __groups = ('project', 'size', 'author', 'entity_structure', 'entity_characteristic', 'complexity', 'relation', 'error','quality','tag','process_log')
    __selection = ('current', 'all')
    # API paths
    __pathLoadGroup = '/load/'
    __pathExtract = '/extract'

    def __init__(self, acct, repo):
        super(Project, self).__init__()
        self.acct = acct
        self.prj_repo_namespace = repo.namespace
        self.prj_repo_email = repo.email
        self.prj_repo_name = repo.repo_name
        for grp in Project.__groups:
            self.__setitem__(grp, 'unavailable')

    # pandas integration methods
    def shape(self):
        tmp = list(self.keys())
        [print(i, ": \n", self[i].shape) for i in tmp]

    def columns(self):
        tmp = list(self.keys())
        [print(i, ": \n", self[i].columns) for i in tmp]


    # API methods
    @time_usage
    def load_group(self, metric_group='project'):
        hdr={'Authorization': 'JWT '+self.acct.token }
        try:
            if metric_group in Project.__groups:
                URI = self.acct._Account__URL +  self._Project__pathLoadGroup + metric_group
                payload = {'namespace':self.prj_repo_namespace, 'email':self.prj_repo_email, 'repo':self.prj_repo_name}
                r = requests.post(URI, data = payload, headers=hdr)
                rec=r.json()['data']
                prec=pandas.DataFrame(rec)
                print(metric_group.upper(),"group records: ",prec.shape[0])
                return prec
            else:
                print(metric_group+" is not an available group")
        except:
            e = sys.exc_info()[0]
            print('there was a problem')
            print( "Error: %s" % e )


    def load_all(self):
        err = []
        for grp in self.keys():
            try:
                tmp = self.load_group(grp)
                self.__setitem__(grp, tmp)
                self.__setattr__(grp, tmp.__getattr__)
            except:
                self.group[grp] = 'unavailable'
                err.append(grp)
        if len(err)>0:
            print("Loading completed with the following groups missing: ",err)
        else:
            print("Loading completed with no errors")

    def extract (self, selection='current'):
        hdr={'Authorization': 'JWT '+self.acct.token }
        try:
            if selection in Project.__selection:
                URI = self.acct._Account__URL + self._Project__pathExtract
                payload = {'namespace':self.prj_repo_namespace, 'email':self.prj_repo_email, 'repo':self.prj_repo_name, 'selection':selection}
                r = requests.post(URI, headers=hdr, data=payload)
                print(r.json()['message'])
                return r
            else:
                print(selection+" is not an available selection")
        except:
            print('there was a problem')
            e = sys.exc_info()[0]
            print('there was a problem')
            print( "Error: %s" % e )







    
    


    

        