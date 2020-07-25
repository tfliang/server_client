## 说明

[TOC]

### 背景

这个项目希望比较异步和多线程在web服务中的效率。

#### server端

server端使用fastapi，是异步的。提供两个测试接口，被调用后会分别执行同步sleep和异步sleep。server为单线程服务。

#### client端

测试不同client端的效率：

- 单线程方式
- 多线程方式
- 异步方式

### 测试结果

5个请求，每个sleep 1秒

- 单线程
  - 同步sleep：5秒
  - 异步sleep：5秒
- 多线程
  - 同步sleep：5秒
  - 异步sleep：1秒
- 异步方式
  - 同步sleep：5秒
  - 异步sleep：1秒

### python多线程与GIL

GIL限制同一时刻只有一个线程占用CPU。对计算密集型的任务，python的多线程是无效的。对于IO密集型任务，由于线程IO操作时，会释放GIL。所以，python的多线程在IO密集型任务中是有效的。但是对于单个线程来说，IO仍然是阻塞的；只是某个线程IO阻塞时，其他线程可以使用CPU。