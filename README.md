# wechatapi文档

## 1.说明
源码来自于微信团队的[https://github.com/sbzhu/weworkapi_python](sbzhu/weworkapi_python)
因为源码是python2的，这里修改成python3的，并先着重使用通讯录管理相关的api，与AD域打通，水平不高，代码质量有待优化

## 2.[https://work.weixin.qq.com/api/doc/90001/90143/90329](企业微信api文档)
源代码很好地将接口写成配置，并做好了错误处理与回退，特别要注意的是有对凭证的请求与刷新机制，其实根据其提供的思路可以很稳健的接着开发了。

## 3.任务
当下的任务有两个，一个是先将代码调试在python3环境没有问题，我会优先先测试完通讯录方面的功能，然后再开展其他部分

另外一个任务是写ad域的api，从ad域那边拉取数据后，再调用企业微信api将通讯录同步

考虑先做一版本，然后在加上定时任务定时同步，或者等清除企业微信api的回调，将回调方面的功能测试使用过会从这方面优先下手
