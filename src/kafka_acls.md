---
# Kafka ACLs

##Cluster Operations

| Operation          | Resource  | Comment |
|--------------------|-----------|---------|
| `ALTER`            | `CLUSTER` | |
| `ALTER_CONFIGS`    | `CLUSTER` | |
| `CLUSTER_ACTION`   | `CLUSTER` | |
| `CREATE`           | `CLUSTER` | |
| `DESCRIBE`         | `CLUSTER` | |
| `DESCRIBE_CONFIGS` | `CLUSTER` | |
| `IDEMPOTENT_WRITE` | `CLUSTER` | |


## Topic Operations

| Operation          | Resource  | Comment |
|--------------------|-----------|---------|
| `ALTER`            | `TOPIC`   | |
| `ALTER_CONFIGS`    | `TOPIC`   | |
| `CREATE`           | `TOPIC`   | |
| `DELETE`           | `TOPIC`   | |
| `DESCRIBE`         | `TOPIC`   | |
| `DESCRIBE_CONFIGS` | `TOPIC`   | |
| `READ`             | `TOPIC`   | |
| `WRITE`            | `TOPIC`   | |

## Group

| Operation          | Resource  | Comment |
|--------------------|-----------|---------|
| `DELETE`           | `GROUP`   | |
| `DESCRIBE`         | `GROUP`   | |
| `READ`             | `GROUP`   | |

# Common Configurations

## Producer
Topic write and describe
WRITE Transactional_id
DESCRIBE Transactional_id
IDEMPTOTENT WRITE Cluster

Create topic
create cluster
describe topic listoffsets
alter topic create partitions

## Consumer
Topic read and describe

read topic
read group

clusteraction cluster fetch partitions data

describe group fetch offsets
describe topic

describe cluster

Consumer GRoups
group groupname read

## Brokers


# References
* https://docs.confluent.io/platform/current/kafka/authorization.html
* https://docs.confluent.io/platform/current/kafka/authorization.html#operations
* https://kafka.apache.org/documentation/#operations_resources_and_protocols
* https://sonamvermani.medium.com/kafka-acls-b1c42df9a7e2
* https://medium.com/@nzaporozhets/getting-started-with-kafka-acls-14b16bbf83d1 !!
