ElasticDeploy :+1:
======

Deploy multiple applications/services/websites on a single AWS Elastic Beanstalk environment.

Unfortunately, there is no easy way to run multiple applications/services/websites, which have their own GIT repository, on a single AWS Elastic Beanstalk environment. ElasticDeploy helps developers to solve that problem.

How does it work?
------
First, you need to create a main deployment repository. Within the root of this repository, ElasticDeploy will store a file called ``edConfig.json``.
This file keeps the information of the external repositories. Each external will be cloned into the main deployment repository (see 'Sample Project Structure').

In addition, all external repositories are automatically added to your .gitignore file. This means that all changes should happen in the external repository itself. It also creates a script in your .ebextensions folder, where all vhosts are added.


Getting Started
------

1. Install ElasticDeploy (PyPI package)  
```pip install ElasticDeploy```  

2. Create new main repository  
```mkdir ed-deployment-repository && cd ed-deployment-repository```  

3. Initialize ElasticDeploy  
```elasticdeploy init```  

4. Follow the initialization guide

5. Create and deploy all applications/services/websites  
```elasticdeploy createAndDeploy```


Sample Project Structure
------

```
ed-deployment-repository
│   .gitignore
│   edConfig.json    
│
└───.git
│
└───.elasticbeanstalk
│       config.yml
│   
└───.ebextensions
│       98ElasticDeploy.config
│
└───project1
│       file1
│       file2
│       subfolder1
│       subfolder2
│   
└───project2
│       file1
│       file2
│       subfolder1
│       subfolder2
│   
└───project3
│       file1
│       file2
│       subfolder1
│       subfolder2
```

All Commands
------

**Show help page**  
```elasticdeploy help```

**Initialize ElasticDeploy**  
```elasticdeploy init```

**Clone all repositories**  
```elasticdeploy cloneAll```

**Add a new repository**  
```elasticdeploy newRepo```

**Clone all repositories**  
```elasticdeploy cloneAll```

**Create application**  
```elasticdeploy create```

**Deploy latest application**  
```elasticdeploy deploy```

**Create and deploy application**  
```elasticdeploy createAndDeploy```



Requirements
------
* [PYTHON](https://www.python.org/downloads/) - Python 2.7  
* [EB-CLI](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html) - Elastic Beanstalk Command Line Interface  
* [GIT](https://git-scm.com/) - GIT Command Line Interface
