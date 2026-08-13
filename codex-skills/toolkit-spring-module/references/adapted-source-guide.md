# 适配后的来源指南

# 快速创建后端模块

## 用途
一键创建Spring Boot service module，分两个阶段：
1. **创建模块**：生成基础目录结构和配置文件
2. **生成业务代码**：按需生成 CRUD 代码、枚举、异常处理等

## 重要说明

**创建新模块时，只生成以下基础文件：**
- pom.xml
- 启动类（Application.java）
- 多环境配置文件（application*.yml）
- 菜单配置文件（application-menu.yml）

**业务代码（Entity、DTO、Mapper、Service、Controller等）在模块创建后，根据实际业务需求按需生成。**

---

## 一、创建模块

### 输入
- **模块名称**: 如 `meizhou`、`digitalvillage`、`partybuilding`
- **模块描述** (可选): 如 "湄洲岛后端接口服务"

### 输出目录结构
```
{backend-prefix}-{module-name}/
├── pom.xml
└── src/main/
    ├── java/com/funo/project/{module-name}/
    │   └── {ModuleName}Application.java
    └── resources/
        ├── application.yml
        ├── application-dev.yml
        ├── application-local.yml
        ├── application-localization.yml
        ├── application-prod.yml
        └── application-menu.yml
```

### 创建步骤

#### 1. 收集信息
- **moduleName**: 模块名称（小写）
- **description**: 模块描述

#### 2. 确认父项目位置
检查当前工作目录是否包含 `pom.xml` 且包含 `project-backend` 父模块。

#### 3. 生成配置文件

| 文件 | 说明 |
|------|------|
| pom.xml | Maven配置 |
| {ModuleName}Application.java | Spring Boot启动类 |
| application.yml | 主配置（含多环境Nacos配置） |
| application-dev.yml | 开发环境配置 |
| application-local.yml | 本地/测试环境配置 |
| application-localization.yml | 国产化环境配置 |
| application-prod.yml | 生产环境配置 |
| application-menu.yml | 菜单配置 |

#### 4. 端口分配
- 基础端口: `38800`
- 计算公式: `port = 38800 + n`（n = 已创建模块数）

#### 5. 添加到父pom.xml
```xml
<module>{backend-prefix}-{module-name}</module>
```

---

## 二、生成业务代码

**业务代码在模块创建后，根据实际需求按需生成。**

### 触发条件
用户明确要求生成特定业务代码，例如：
- "生成标签管理的CRUD代码"
- "创建Tag实体和相关代码"
- "添加Excel导入功能"

### 可生成的代码类型

#### 1. CRUD链路代码
| 模板 | 说明 | 触发词示例 |
|------|------|-----------|
| Entity.java | 实体类 | "生成实体类" |
| DTO.java | 数据传输对象 | "生成DTO" |
| Mapper.java | Mapper接口 | "生成Mapper" |
| Mapper.xml | Mapper XML | "生成Mapper XML" |
| Service.java | Service接口 | "生成Service" |
| ServiceImpl.java | Service实现 | "生成Service实现" |
| Controller.java | 控制器 | "生成Controller" |

#### 2. 枚举类
| 模板 | 说明 | 触发词示例 |
|------|------|-----------|
| ErrorEnum.java | 错误码枚举 | "生成错误枚举" |
| CommonEnum.java | 通用枚举 | "生成状态枚举" |

#### 3. 异常处理
| 模板 | 说明 | 触发词示例 |
|------|------|-----------|
| ValidationException.java | 自定义校验异常 | "生成异常处理" |
| GlobalExceptionHandler.java | 全局异常处理器 | "生成全局异常处理" |

#### 4. Excel相关
| 模板 | 说明 | 触发词示例 |
|------|------|-----------|
| ImportDTO.java | Excel导入对象 | "生成Excel导入" |
| ExcelVO.java | Excel导出对象 | "生成Excel导出" |
| ImportListener.java | Excel导入监听器 | "生成导入监听器" |

#### 5. 其他
| 模板 | 说明 | 触发词示例 |
|------|------|-----------|
| VO.java | 视图对象 | "生成VO" |
| FeignClient.java | Feign客户端 | "生成Feign客户端" |
| XxlJobConfig.java | XXL-JOB配置 | "生成定时任务配置" |

---

## 三、占位符说明

### 通用占位符
| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{module-name}` | 模块名称（小写） | `grid2` |
| `{ModuleName}` | 模块名称（PascalCase） | `Grid2` |
| `{business}` | 业务包名 | `tag` |
| `{EntityName}` | 实体类名（PascalCase） | `Tag` |
| `{entity-name}` | 实体名称（kebab-case） | `tag` |
| `{description}` | 业务描述 | `标签管理` |
| `{table-name}` | 数据库表名 | `tag` |
| `{port}` | 服务端口 | `38801` |

### 配置文件占位符
| 占位符 | 说明 |
|--------|------|
| `{datasource-ip}` | 数据库IP:端口 |
| `{datasource-username}` | 数据库用户名 |
| `{datasource-password}` | 数据库密码 |
| `{datasource-database}` | 数据库名称 |
| `{redis-nodes}` | Redis集群节点 |
| `{redis-password}` | Redis密码 |
| `{nacos-addr-*}` | 各环境Nacos地址 |
| `{nacos-username-*}` | 各环境Nacos用户名 |
| `{nacos-password-*}` | 各环境Nacos密码 |
| `{xxl-*}` | XXL-JOB相关配置 |

---

## 四、使用示例

### 示例1: 创建新模块
```
用户: 创建数字乡村模块 digitalvillage

输出:
✅ 模块 project-backend-digitalvillage 创建成功!

📁 生成的文件:
├── pom.xml
└── src/main/
    ├── java/com/funo/project/digitalvillage/
    │   └── DigitalvillageApplication.java
    └── resources/
        ├── application.yml
        ├── application-dev.yml
        ├── application-local.yml
        ├── application-localization.yml
        ├── application-prod.yml
        └── application-menu.yml

⚠️  下一步:
1. 调整数据库配置
2. 根据业务需求生成代码
3. 执行 mvn clean install
```

### 示例2: 生成CRUD代码
```
用户: 在 digitalvillage 模块中生成标签管理代码，实体名 Tag，表名 tag

输出:
✅ 业务代码生成成功!

📁 生成的文件:
├── src/main/java/com/funo/project/digitalvillage/
│   ├── controller/TagController.java
│   ├── service/tag/
│   │   ├── ITagService.java
│   │   └── impl/TagServiceImpl.java
│   ├── mapper/TagMapper.java
│   └── entity/tag/
│       ├── Tag.java
│       └── TagDTO.java
└── src/main/resources/mapper/TagMapper.xml
```

### 示例3: 生成Excel导入功能
```
用户: 为标签管理生成Excel导入功能

输出:
✅ Excel导入功能生成成功!

📁 生成的文件:
├── entity/tag/
│   ├── TagImportDTO.java
│   ├── TagExcelVO.java
│   └── listener/TagImportListener.java
```

---

## 五、代码规范

### Entity 规范
- 使用 Lombok 注解: `@Data`, `@Builder`, `@AllArgsConstructor`, `@NoArgsConstructor`
- 主键使用 `@JsonFormat(shape = JsonFormat.Shape.STRING)` 防止精度丢失
- 包含通用字段: `id`, `tenantId`, `isDel`, `createTime`, `updateTime`, `createBy`, `updateBy`

### DTO 规范
- 使用 Jakarta Validation 注解进行参数校验
- 只包含需要传输的字段

### Service 规范
- 接口继承 `IService<Entity>`
- 实现类继承 `ServiceImpl<Mapper, Entity>`
- 使用 LambdaQueryWrapper/LambdaUpdateWrapper 进行查询

### Controller 规范
- 添加 `@RestController` 和 `@RequestMapping`
- 添加 `@ApiResource` 注解配置权限
- 使用 `Result` 统一返回格式
- 提供标准的 CRUD 接口: `/list`, `/detail/{id}`, `/add`, `/update`, `/delete/{id}`

### Excel 导入导出规范
- ImportDTO: 使用 `@ExcelProperty` + `@Excel` 双注解，必填项前加 `*`
- ExcelVO: 使用 `@Excel` 注解（EasyPoi）
- ImportListener: 继承 `AnalysisEventListener`

### 异常处理规范
- `ValidationException` 继承 `BussinessException`
- 业务异常返回具体信息，系统异常返回通用信息

---

## 六、注意事项

### 模块创建
- 始终使用 `com.funo.project.{module-name}` 作为Java包名
- 模块名使用小写字母
- 类名首字母大写 (PascalCase)
- 启动类添加 `@SpringBootApplication`, `@EnableAsync`, `@EnableScheduling`, `@EnableDiscoveryClient`
- **application.yml 已整合多环境Nacos配置**

### 业务代码生成
- 业务代码按需生成，不是创建模块时自动生成
- 删除操作使用逻辑删除（设置 `is_del = '1'`）
- 多租户场景自动注入 `tenantId`
- 审计字段自动填充（createBy、createTime等）
