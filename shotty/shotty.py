import sys
import boto3
import click as click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')


def filter_instances(project):
    
    if project:
        filters = [{'Name': 'tag:Project', 'Values': [project]}]
        inst = ec2.instances.filter(Filters=filters)
    else:
        inst = ec2.instances.all()

    return inst


@click.group()
def instances():
    """ Commands for instances """


@instances.command('list')
@click.option('--project', default=None,
              help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    """ List EC2 instances """

    inst = filter_instances(project)

    for i in inst:
        tags = {t['Key']: t['Value'] for t in i.tags or []}
        print(','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
        )))

    return


@instances.command('stop')
@click.option('--project', default=None, help='Only instances for project')
def stop_instances(project):
    """ Stop EC2 instances """

    inst = filter_instances(project)

    for i in inst:
        print("Stopping {0}...".format(i.id))
        i.stop()


@instances.command('start')
@click.option('--project', default=None, help='Only instances for project')
def start_instances(project):
    """ Start EC2 instances """

    inst = filter_instances(project)

    for i in inst:
        print("Starting {0}...".format(i.id))
        i.start()


if __name__ == '__main__':
    # print(sys.argv)
    instances()
