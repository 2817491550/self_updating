
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [基础](#基础)
  - [kubernetes：](#kubernetes)
  - [特点](#特点)
  - [为什么](#为什么)
  - [能做什么](#能做什么)
- [概念](#概念)
  - [组件](#组件)
    - [1. Master组件](#1-master组件)
      - [01 kube-apiserver](#01-kube-apiserver)
      - [02 ETCD](#02-etcd)
      - [03 kube-controller-manager](#03-kube-controller-manager)
      - [04 cloud-controller-manager](#04-cloud-controller-manager)
      - [05 kube-scheduler](#05-kube-scheduler)
      - [06 addons](#06-addons)
      - [07 DNS](#07-dns)
      - [08 用户界面](#08-用户界面)
      - [09 容器资源监测](#09-容器资源监测)
      - [10 Cluster-level Logging](#10-cluster-level-logging)
    - [2. Node组件](#2-node组件)
      - [01 kubelet](#01-kubelet)
      - [02 kube-proxy](#02-kube-proxy)
      - [03 docker](#03-docker)
      - [04 supervisord](#04-supervisord)
      - [05 fluentd](#05-fluentd)

<!-- /code_chunk_output -->

# 基础
## kubernetes：
    容器集群管理系统，可实现容器集群的自动化部署、自动化扩缩容、维护。

    快速部署、快速拓展
    无缝对接新应用功能
    节省资源、优化硬件资源的使用
## 特点
    可移植：支持公有云、私有云、混合云、多重云
    可拓展：模块化、插件化、可挂载、可组合
    自动化：自动部署、重启、复制、扩缩容
## 为什么
1. bad thing about old way：
a. 应用运行、配置、管理、生存周期将和当前OS绑定，不利于应用的升级、回滚。
b. 虚拟机较重。
2. good thing about new way:
a. 每个容器之间互相隔离，每个容器有自己的文件系统，容器之间进程不会相互影响，可区分计算资源。
b. 相比于虚拟机，容器可以快速部署；由于容器与底层设施、机器文件系统解耦，所以可以在不同云、不同操作系统版本之间迁移。

## 能做什么
    可以在k8s集群上运行容器化应用，k8s提供一个以“容器为中心的基础架构”，可满足：
    1. 多进程(作为容器运行)协同工作。(Pod)
    2. 存储系统挂载
    3. Distributing secrets
    4. 应用健康监测
    5. 应用实例的复制
    6. Pod自动扩缩容
    7. Naming and discovering
    8. 负载均衡
    9. 滚动更新
    10. 资源监控
    11. 日志访问
    12. 调试
    13. 认证&授权

# 概念
## 组件
### 1. Master组件
    提供集群的管理控制中心。可以在集群的任何节点上运行。
#### 01 kube-apiserver
    用于暴露k8s-api。任何资源请求/调用操作都是通过其提供的接口进行。
#### 02 ETCD
    k8s提供默认的存储系统。
#### 03 kube-controller-manager
    运行管理控制器，是集群中处理常规任务的后台进程。

    包括：
        节点控制器
        副本控制器：用于维护系统中每个副本中的pod
        端点控制器：填充endpoints对象（连接services和pods）
        service account&token控制器：为新的namespace创建默认账户访问api-token。
#### 04 cloud-controller-manager
    负责与底层云提供商的平台交互。
    包括：
        节点控制器
        路由控制器
        service控制器
        卷控制器
#### 05 kube-scheduler
    监视新创建没有分配到Node的Pod，为Pod选择一个Node。
#### 06 addons
    实现集群Pod和services功能。
    Pod由Deployments、ReplicationController管理。
#### 07 DNS
#### 08 用户界面
#### 09 容器资源监测
#### 10 Cluster-level Logging
### 2. Node组件
    运行在Node，提供k8s运行时环境，以及维护pod
#### 01 kubelet
    主要的节点代理，监视已分配给节点的pod
#### 02 kube-proxy
#### 03 docker
#### 04 supervisord
#### 05 fluentd