from subprocess import call
from helpers import getCurrentConfigFile, cloneRepo, addRepo, checkEbInit, createBasicConfigFile, runCommandsBeforeApplicationCreation, createApplication, updateArtifact, getPathToApplicationFolder


def showHelp():
    print "Help is still in progress. Sorry."


def initialize():
    print "Hey, let's initialize your ElasticDeploy Repository"

    checkEbInit()
    createBasicConfigFile()
    addRepo(True)

    print "\n\nConfiguration done! Now run 'ed create'\n\n"


def cloneAll():
    configFile = getCurrentConfigFile()
    repositories = configFile["repositories"]

    for repo in repositories:
        cloneRepo(repo["path"])


def newRepo():
    addRepo(False)


def create():
    try:
        print "Starting ElasticDeploy"
        runCommandsBeforeApplicationCreation()

        # Create application (.zip folder in multiDeployLib/applications)
        applicationName = createApplication()

        # Update Artifact
        updateArtifact(getPathToApplicationFolder() + applicationName)

        print "\n\n!! Now is a good time to test your final build. Afterwards you can deploy it with 'ed deploy' !!\n\n"

    except KeyError:
        print "\nSomething is wrong with your config. Did you already initialize your project with 'ed init'?\n"

    except:
        print "\n\nAn error happened. Bye bye!"


def deploy():
    print "\n\n!! Application gets deployed !!\n\n"
    call(["eb", "deploy"])
