# :electric_plug: :jigsaw: Clean Architecture FastAPI Project Template

[![Python 3.9–3.13](https://img.shields.io/badge/Python-3.9--3.13-000000?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)[![GitHub Stars](https://img.shields.io/github/stars/Peopl3s/clean-architecture-fastapi-project-template?style=for-the-badge&logo=github&logoColor=white&color=000000)](https://github.com/Peopl3s/clean-architecture-fastapi-project-template/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Peopl3s/clean-architecture-fastapi-project-template?style=for-the-badge&color=000000)](https://github.com/Peopl3s/clean-architecture-fastapi-project-template/commits/main)
[![License](https://img.shields.io/github/license/Peopl3s/clean-architecture-fastapi-project-template?style=for-the-badge&color=000000)](./LICENSE)

![FastAPI](https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi&logoColor=white)
![FastStream](https://img.shields.io/badge/FastStream-000000?style=for-the-badge&logo=faststream&logoColor=white)
![Dishka](https://img.shields.io/badge/Dishka-000000?style=for-the-badge&logoColor=white)
![Clean Architecture](https://img.shields.io/badge/Clean_Architecture-000000?style=for-the-badge&logo=python&logoColor=white)


A comprehensive cookiecutter template for creating modern FastAPI applications with clean architecture, Docker support, and best practices included.

:dizzy: Litestar Clean Acrhitecture Project Template - https://github.com/Peopl3s/clean-architecture-litestar-project-template

## 🚀 Features

- **Clean Architecture**: Domain-Driven Design with clear separation of concerns
- **FastAPI**: High-performance async web framework
- **SQLAlchemy**: Modern ORM with async support
- **Unit of Work**: Transaction management and coordination
- **Database Support**: Optional database support (PostgreSQL/SQLite/MySQL)
- **Alembic**: Database migration management
- **Docker**: Complete containerization with Docker Compose
- **Caching System**: Optional caching support (Redis/KeyDB/Tarantool/Dragonfly)
- **Message Broker**: Optional message broker support (Kafka/RabbitMQ/NATS) via [FastStream](https://github.com/ag2ai/faststream)
- **Testing**: Comprehensive test suite with pytest
- **Code Quality**: Ruff for linting, MyPy for type checking
- **Pre-commit**: Git hooks for code quality
- **Documentation**: Auto-generated API docs with Swagger/OpenAPI
- **DI**: Powered by [dishka](https://github.com/reagento/dishka)

## 🚀 Quick Start

```bash
 cookiecutter . --no-input \
  project_name="My Awesome API" \
  project_description="An awesome API for my project" \
  author_name="John Doe" \
  author_email="john@example.com" \
  github_username="johndoe" \
  domain_name="awesomeapi.com" \
  use_broker="kafka" \
  use_cache="redis" \
  use_database="postgresql" \
  add_docker="y" \
  add_tests="y" \
  add_docs="y" \
  add_precommit="y" \
  license_type="MIT"

  cd my_awesome_api

  make dev-setup-docker

  make docker-up-dev

```

## 📚 Documentation

### Building Documentation Locally

```bash
cd docs
pip install -r requirements.txt
make html
open _build/html/index.html  # macOS
# or
xdg-open _build/html/index.html  # Linux
```

## 🛠️ Usage

### Basic Usage

```bash
cookiecutter https://github.com/Peopl3s/clean-architecture-fastapi-project-template.git
```

### Local Usage

```bash
# Clone the template
git clone https://github.com/Peopl3s/clean-architecture-fastapi-project-template.git
cd clean-architecture-fastapi-project-template

# Use the template
cookiecutter .
```

## ⚙️ Template Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `project_name` | Name of the project | "My FastAPI Project" | Yes |
| `project_slug` | Slugified project name (auto-generated) | - | No |
| `project_description` | Short description of the project | "A modern FastAPI application..." | Yes |
| `author_name` | Author's name | "Your Name" | Yes |
| `author_email` | Author's email | "your.email@example.com" | Yes |
| `github_username` | GitHub username | "yourusername" | Yes |
| `version` | Project version | "0.1.0" | No |
| `database_name` | Database name | `{project_slug}` | No |
| `database_user` | Database username | `{project_slug}_user` | No |
| `database_password` | Database password | `{project_slug}_password` | No |
| `redis_password` | Redis password | "redis_password" | No |
| `api_title` | API title | `{project_name} API` | No |
| `api_version` | API version | "1.0.0" | No |
| `api_description` | API description | "API for {project_description}" | No |
| `domain_name` | Domain name for APIs | "example.com" | Yes |
| `use_broker` | Choose message broker type | `["none", "kafka", "rabbitmq", "nats"]` | No |
| `use_cache` | Choose caching system type | `["none", "redis", "keydb", "tarantool", "dragonfly"]` | No |
| `use_database` | Choose database type | `["none", "postgresql", "sqlite", "mysql"]` | No |
| `add_docker` | Add Docker configuration | "y" | No |
| `add_tests` | Add test suite | "y" | No |
| `add_docs` | Add documentation | "y" | No |
| `add_precommit` | Add pre-commit hooks | "y" | No |
| `license_type` | License type | "MIT" | No |

## 🏗️ Generated Project Structure

```
{{cookiecutter.project_slug}}/
├── 📁 src/                          # Source code
│   ├── 📁 domain/                   # Domain layer (business logic)
│   │   ├── 📁 entities/             # Domain entities
│   │   ├── 📁 value_objects/        # Value objects
│   │   ├── 📁 services/             # Domain services
│   │   └── exceptions.py            # Domain exceptions
│   ├── 📁 application/              # Application layer
│   │   ├── 📁 use_cases/            # Use cases
│   │   ├── 📁 dtos/                 # Data transfer objects
│   │   ├── 📁 interfaces/           # Application interfaces
│   │   └── exceptions.py            # Application exceptions
│   ├── 📁 presentation/             # Presentation layer
│   │   └── 📁 api/                  # API endpoints
│   │   └── 📁 cli/                  # CLI endpoints
│   ├── 📁 infrastructures/          # Infrastructure layer
│   │   ├── 📁 db/                   # Database implementations
│   │   ├── 📁 cache/                # Cache implementations
│   │   └── 📁 broker/               # Message broker implementations
│   │   └── 📁 mappers/              # Infrastructure mappers
│   └── 📁 config/                   # Configuration
│       ├── 📁 ioc/                  # Dependency injection
│       ├── app.py                   # Core application settings
│       ├── database.py              # Database configuration
│       ├── redis.py                 # Redis cache configuration
│       ├── external_apis.py         # External API settings
│       ├── broker.py                # Message broker configuration
│       ├── cors.py                  # CORS configuration
│       ├── settings.py              # Main settings facade
│       └── base.py                  # Backward compatibility wrapper
├── 📁 tests/                        # Test suite
├── 📁 docs/                         # Documentation
├── 📁 scripts/                      # Utility scripts
├── pyproject.toml                   # Project configuration
├── docker-compose.yml               # Docker services
├── Dockerfile                       # Container configuration
├── env.template                     # Environment variables template
├── .pre-commit-config.yaml          # Pre-commit hooks
├── .gitignore                       # Git ignore rules
└── README.md                        # Project documentation
```


## 📚 API Documentation

Once your application is running, access the API documentation at:

- **Swagger UI**: `http://localhost:8000/api/docs`
- **ReDoc**: `http://localhost:8000/api/redoc`
- **OpenAPI Schema**: `http://localhost:8000/api/openapi.json`

## 🛠️ Development Commands

### Dependencies

```bash
# Install main dependencies
pip install -e .

# Install development dependencies
pip install --dependency-group dev

# Install all dependencies (alternative)
pip install -e ".[dev]"

# Check dependency versions
pip list
```

### Code Quality

```bash
make lint          # Run linter
make lint-fix     # Fix linting issues
make format        # Format code
make type-check    # Run type checker
make check         # Run all checks
```

### Testing

```bash
make test          # Run tests
make test-cov      # Run tests with coverage
make docker-test   # Run tests in Docker
```

### Database

```bash
make migration msg="Description"  # Create migration
make migrate                      # Apply migrations
make migrate-downgrade            # Rollback migration
```

### Docker

```bash
make docker-build    # Build Docker image
make docker-up-dev   # Start development environment
make docker-down     # Stop all services
make docker-logs     # View logs
```

## 🏗️ Architecture Overview

The template follows **Clean Architecture** principles with clear separation of concerns:

### Domain Layer
- **Entities**: Core business objects
- **Value Objects**: Immutable domain types
- **Services**: Business logic that doesn't fit in entities
- **Exceptions**: Domain-specific exceptions

### Application Layer
- **Use Cases**: Application-specific business rules
- **DTOs**: Data transfer objects using plain dataclasses with validation in `__post_init__` (Pydantic-free)
- **Interfaces**: Abstractions for infrastructure implementations (repositories, mappers, serialization, etc.)
- **Unit of Work**: Transaction management and coordination
- **Mappers**: Convert between domain entities and application DTOs (no serialization logic)

### Presentation Layer
- **API Controllers**: Handle HTTP requests and responses
- **Response Schemas**: Pydantic models for API responses (no validation logic)
- **Presentation Mappers**: Convert application DTOs to response models
- **Middleware**: Cross-cutting concerns
- **Routers**: URL routing configuration

### Infrastructure Layer
- **Repositories**: Data access implementations
- **Cache**: Caching service implementations
- **Message Brokers**: External service integrations using dictionary serialization
- **HTTP Clients**: External API integrations using dictionary serialization
- **Infrastructure Mappers**: Convert between application DTOs and dictionaries for external API communication, handle JSON serialization

## 🔄 Unit of Work

The template includes a **Unit of Work** implementation that provides transaction management and coordination for database operations.

### 🎯 Key Features

#### **Transaction Management**
- **Atomic Operations**: All changes are committed or rolled back as a single unit
- **Context Manager Support**: Automatic transaction management with async context managers
- **Error Handling**: Automatic rollback on transaction failures
- **Async Support**: Full async/await support for modern Python applications

## 🔄 Advanced Unit of Work with Identity Map

The template also includes an advanced **Unit of Work** implementation that follows the **Identity Map** pattern for efficient change tracking and transaction management.

### 🎯 Key Features

#### **Identity Map Pattern**
- **Object Tracking**: Maintains a map of all objects loaded during a business transaction
- **Change Detection**: Automatically tracks modifications to registered objects
- **Duplicate Prevention**: Ensures each object is loaded only once per transaction
- **Performance Optimization**: Reduces database queries and prevents unnecessary updates

#### **Automatic Dirty Tracking**
- **UoWModel Wrapper**: Special wrapper class that automatically marks objects as dirty when modified
- **Transparent Integration**: Works seamlessly with existing domain models
- **Attribute Monitoring**: Intercepts attribute changes and registers objects for updates

#### **Transaction Management**
- **Atomic Operations**: All changes are committed or rolled back as a single unit
- **Batch Processing**: Optimizes database operations by batching inserts, updates, and deletes
- **Error Handling**: Automatic rollback on transaction failures

### 🏗️ Architecture

```python
# Core Unit of Work implementation
class UnitOfWork:
    def __init__(self):
        self.dirty = {}      # Modified objects
        self.new = {}        # New objects to insert
        self.deleted = {}    # Objects to delete
        self.mappers = {}    # Database mappers

    def register_new(self, model) -> UoWModel:
        """Register a new model and return a tracked wrapper."""
        
    def register_dirty(self, model) -> None:
        """Mark a model as modified."""
        
    def register_deleted(self, model) -> None:
        """Mark a model for deletion."""
        
    def commit(self) -> None:
        """Commit all changes to the database."""
```

### 📝 Usage Examples

#### **Basic Usage**
```python
# Create Unit of Work
uow = UnitOfWork()

# Register new entity
artifact = ArtifactModel(name="Ancient Vase", era="ANCIENT")
uow_artifact = uow.register_new(artifact)

# Modify through wrapper (automatically tracked)
uow_artifact.name = "Updated Ancient Vase"

# Commit all changes
uow.commit()
```

#### **Custom Mappers**
```python
# Register custom mappers for different model types
uow.register_mapper(CustomModel, CustomModelMapper(session))

# The Unit of Work will use appropriate mappers for each model type
```

### 🔧 Implementation Details

#### **UoWModel Wrapper**
- **Transparent Proxy**: Acts as a proxy to the underlying model
- **Change Detection**: Intercepts attribute modifications
- **Automatic Registration**: Automatically registers objects as dirty when modified
- **Type Safety**: Maintains type hints and IDE support

#### **Database Mapper Protocol**
- **Standardized Interface**: `DbMapperProtocol` defines the contract for all mappers
- **CRUD Operations**: Standard `insert`, `update`, `delete` methods
- **Extensibility**: Easy to add new mappers for different model types
- **Testability**: Protocol-based design enables easy mocking

### 🎯 Benefits

1. **Performance**: Reduces database queries through intelligent change tracking
2. **Consistency**: Ensures data consistency through atomic transactions
3. **Simplicity**: Easy-to-use API with automatic change detection
4. **Flexibility**: Extensible mapper system for different data sources
5. **Reliability**: Comprehensive error handling and rollback support
6. **Testability**: Protocol-based design enables easy testing and mocking

## 🔄 Alternative Naming Conventions in Clean Architecture

### 📋 Overview

Clean Architecture, while conceptually consistent, has evolved various naming conventions across different teams, organizations, and architectural schools. This section helps developers understand the terminology they might encounter when working with different codebases or reading architectural literature.

### 🏗️ Layer Alternative Names

#### **Domain Layer** (Core/Business Layer)
| Common Name | Alternative Names | Context/Usage |
|-------------|-------------------|---------------|
| **Domain Layer** | Core Layer, Business Layer | Most common in enterprise applications |
| **Entities** | Business Objects, Domain Models | "Business Objects" is common in older systems |
| **Value Objects** | Immutable Objects, Value Types | "Immutable Objects" emphasizes the immutability aspect |
| **Domain Services** | Business Services, Core Services | "Business Services" is more descriptive for non-technical stakeholders |
| **Aggregates** | Aggregate Roots, Bounded Contexts | "Bounded Contexts" is from DDD, broader concept |

#### **Application Layer** (Use Cases/Service Layer)
| Common Name | Alternative Names | Context/Usage |
|-------------|-------------------|---------------|
| **Application Layer** | Service Layer, Use Case Layer | "Service Layer" is very common in enterprise Java |
| **Use Cases** | **Interactors**, Application Services, Operations | "Interactors" is popular in iOS/Mac development |
| **DTOs** | Data Transfer Objects, View Models, Request/Response Models | "View Models" is common in MVC/MVVM patterns |
| **Application Services** | Orchestrators, Coordinators, Workflow Services | "Orchestrators" emphasizes coordination role |
| **Mappers** | Converters, Transformers, Adapters | "Converters" is simpler and more direct |

#### **Presentation Layer** (Interface/Adapter Layer)
| Common Name | Alternative Names | Context/Usage |
|-------------|-------------------|---------------|
| **Presentation Layer** | Interface Layer, Adapter Layer, UI Layer | "Interface Layer" is from original Clean Architecture |
| **Controllers** | Handlers, Presenters, Endpoints | "Handlers" is common in message-based systems |
| **APIs** | Endpoints, Routes, Resources | "Endpoints" is common in REST API documentation |
| **Middleware** | Interceptors, Filters, Pipes | "Interceptors" is common in Java EE frameworks |
| **Serializers** | Marshallers, Parsers, Formatters | "Marshallers" is common in XML/JSON processing |

#### **Infrastructure Layer** (Data/External Layer)
| Common Name | Alternative Names | Context/Usage |
|-------------|-------------------|---------------|
| **Infrastructure Layer** | Data Layer, External Layer, Technical Layer | "Data Layer" is common in simple CRUD applications |
| **Repositories** | **Gateways**, Data Access Objects (DAO), Stores | "Gateways" is from original Clean Architecture |
| **Database Models** | Entity Models, Persistence Models, Table Models | "Persistence Models" emphasizes the persistence aspect |
| **External Services** | Third-party Services, External APIs, Integrations | "Integrations" is common in enterprise systems |
| **Caching** | Cache Store, Memory Store, Performance Layer | "Cache Store" is more specific about implementation |

### 🔄 Component Alternative Names

#### **Data Access Patterns**
| Pattern | Alternative Names | When to Use |
|---------|-------------------|-------------|
| **Repository** | Gateway, DAO, Store, Persistence Layer | "Gateway" for abstract data access, "DAO" for database-specific |
| **Unit of Work** | Transaction Manager, Session Manager, Context | "Transaction Manager" when focusing on ACID properties |
| **Query Object** | Specification, Criteria, Query Builder | "Specification" when following DDD patterns |
| **Data Mapper** | Object Mapper, Entity Mapper, Converter | "Object Mapper" is more generic |

#### **Business Logic Patterns**
| Pattern | Alternative Names | When to Use |
|---------|-------------------|-------------|
| **Use Case** | Interactor, Application Service, Operation | "Interactor" in mobile apps, "Application Service" in enterprise |
| **Domain Service** | Business Service, Core Service, Rule Engine | "Business Service" for clarity with business stakeholders |
| **Aggregate** | Aggregate Root, Bounded Context, Entity Cluster | "Bounded Context" for larger domain boundaries |
| **Factory** | Builder, Creator, Constructor | "Builder" when complex object construction is needed |

#### **Integration Patterns**
| Pattern | Alternative Names | When to Use |
|---------|-------------------|-------------|
| **Message Broker** | Event Bus, Message Queue, Pub/Sub System | "Event Bus" for event-driven architectures |
| **API Client** | HTTP Client, Service Client, External Client | "Service Client" when working with multiple services |
| **Cache Client** | Cache Store, Memory Cache, Performance Layer | "Cache Store" for specific implementation focus |
| **Serializer** | Marshaller, Parser, Formatter, Encoder/Decoder | "Marshaller" for XML/JSON, "Parser" for text data |

### 📚 Architectural School Variations

#### **Robert C. Martin (Uncle Bob) - Original Clean Architecture**
- Emphasizes "Entities" and "Use Cases"
- Uses "Interface Adapters" for presentation
- "Frameworks & Drivers" for infrastructure
- Focus on dependency rule: "Dependencies point inward"

#### **Domain-Driven Design (DDD)**
- Emphasizes "Aggregates" and "Bounded Contexts"
- "Domain Services" for business logic
- "Application Services" for use case coordination
- "Repositories" for aggregate persistence

#### **Hexagonal Architecture (Ports & Adapters)**
- "Ports" instead of interfaces
- "Adapters" instead of implementations
- "Application Core" instead of domain/application layers
- Focus on "inside-out" development

#### **Onion Architecture**
- "Domain Model" at center
- "Domain Services" surrounding domain
- "Application Services" outer layer
- "Infrastructure" outermost layer

### 🎯 Choosing the Right Terminology

#### **For Your Team**
1. **Be Consistent**: Choose one naming convention and stick to it
2. **Document Your Choice**: Add a glossary to your project documentation
3. **Consider Your Background**: Use terminology familiar to your team
4. **Think About Newcomers**: Choose names that are self-explanatory

#### **For Different Contexts**
1. **Business Stakeholders**: Use "Business Services", "Data Stores", "User Interfaces"
2. **Technical Team**: Use "Use Cases", "Repositories", "Controllers"
3. **Cross-Team Communication**: Use more generic terms like "Services", "Data Layer", "API Layer"

#### **Best Practices**
1. **Create a Glossary**: Document your naming conventions
2. **Use Code Comments**: Explain non-obvious naming choices
3. **Review Regularly**: Ensure consistency across the codebase
4. **Educate New Team Members**: Include architectural terminology in onboarding

### 📖 Quick Reference

| Layer | Primary Name | Common Alternatives | Most Popular Alternative |
|-------|--------------|---------------------|--------------------------|
| Domain | Domain Layer | Core Layer, Business Layer | **Core Layer** |
| Application | Application Layer | Service Layer, Use Case Layer | **Service Layer** |
| Presentation | Presentation Layer | Interface Layer, UI Layer | **Interface Layer** |
| Infrastructure | Infrastructure Layer | Data Layer, Technical Layer | **Data Layer** |

| Component | Primary Name | Common Alternatives | Most Popular Alternative |
|-----------|--------------|---------------------|--------------------------|
| Use Case | Use Case | Interactor, Application Service | **Interactor** |
| Repository | Repository | Gateway, DAO | **Gateway** |
| Controller | Controller | Handler, Endpoint | **Handler** |
| DTO | DTO | View Model, Request/Response Model | **View Model** |

This reference helps when reading different architectural blogs, books, or when joining new teams that might use different terminology for the same concepts.

## 🔧 Configuration

### Environment Variables

The template uses environment variables for configuration. Copy `env.template` to `.env` and customize:

```bash
# Application
ENVIRONMENT=dev
LOG_LEVEL=DEBUG
DEBUG=true

# Database (if enabled)
# PostgreSQL
POSTGRES_USER={{cookiecutter.database_user}}
POSTGRES_PASSWORD={{cookiecutter.database_password}}
POSTGRES_DB={{cookiecutter.database_name}}

# SQLite
SQLITE_DB_PATH={{cookiecutter.database_name}}.db
SQLITE_DB_DIR=./data

# MySQL
MYSQL_USER={{cookiecutter.database_user}}
MYSQL_PASSWORD={{cookiecutter.database_password}}
MYSQL_DB={{cookiecutter.database_name}}

# Redis (if enabled)
REDIS_PASSWORD={{cookiecutter.redis_password}}

# External APIs
MUSEUM_API_BASE=https://api.{{cookiecutter.domain_name}}
CATALOG_API_BASE=https://catalog.{{cookiecutter.domain_name}}
```

### Dependency Injection

The template uses **Dishka** for dependency injection. Providers are configured in `src/config/ioc/providers.py`.

## 🧪 Testing

The template includes a comprehensive test suite:

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **API Tests**: Test HTTP endpoints
- **Infrastructure Tests**: Test database and cache operations

Run tests with coverage:
```bash
make test-cov
```

## 🐳 Docker Support

The template includes complete Docker configuration:

- **Development**: Hot-reload development environment
- **Production**: Optimized production build
- **Testing**: Isolated test environment
- **Migrations**: Database migration runner

Services included:
- **Database**: Database support (PostgreSQL, SQLite, or MySQL, optional)
- **Caching System**: Caching support (Redis, KeyDB, Tarantool, or Dragonfly, optional)
- **Message Broker**: Message broker support (Kafka/Zookeeper, RabbitMQ, or NATS, optional)
- **Application**: FastAPI application

## 📝 Implementation Examples

The template includes comprehensive implementation examples that demonstrate best practices:

#### Domain Layer Examples
- **Entity Implementation**: `src/domain/entities/artifact.py` - Shows how to create domain entities with business logic
- **Value Objects**: `src/domain/value_objects/era.py` and `src/domain/value_objects/material.py` - Demonstrates immutable value objects with validation
- **Domain Services**: Examples of business logic that doesn't fit in entities

#### Application Layer Examples
- **Use Cases**: `src/application/use_cases/process_artifact.py` - Shows how to implement business logic using dependency injection and Protocol-based dependencies
- **DTOs**: `src/application/dtos/artifact.py` - Data transfer objects using plain dataclasses with validation in `__post_init__` methods (Pydantic-free)
- **Interfaces**: Complete interface definitions for repositories, cache, HTTP clients, message brokers, mappers, and serialization
- **Mappers**: `src/application/mappers.py` - Examples of converting between domain entities and DTOs (no serialization logic)

#### Infrastructure Layer Examples
- **Repository Implementation**: `src/infrastructures/db/repositories/artifact.py` - Shows how to implement repository pattern with SQLAlchemy
- **Cache Implementation**: `src/infrastructures/cache/redis_client.py` - Redis caching implementation with error handling
- **HTTP Clients**: `src/infrastructures/http/clients.py` - External API integration examples using dictionary serialization
- **Database Models**: `src/infrastructures/db/models/artifact.py` - SQLAlchemy model examples
- **Infrastructure Mappers**: `src/infrastructures/mappers/artifact.py` - Mappers for converting between application DTOs and dictionaries for external API communication, plus JSON serialization/deserialization

#### Presentation Layer Examples
- **REST Controllers**: `src/presentation/api/rest/v1/controllers/artifact_controller.py` - API endpoint implementation with proper dependency injection
- **Response Schemas**: `src/presentation/api/rest/v1/schemas/responses.py` - Pydantic response models (no validation logic)
- **Presentation Mappers**: `src/presentation/api/rest/v1/mappers/artifact_mapper.py` - Mappers for converting DTOs to response models
- **Exception Handling**: `src/presentation/api/rest/v1/exceptions.py` - Custom exception handlers
- **Middleware**: `src/presentation/api/rest/middlewares.py` - Request/response middleware examples

#### Configuration Examples
- **Dependency Injection**: `src/config/ioc/providers.py` - Complete DI container setup
- **Configuration Management**: `src/config/base.py` - Environment-based configuration
- **Logging Setup**: `src/config/logging.py` - Structured logging configuration

#### Testing Examples
- **Unit Tests**: `tests/test_domain/test_entities/test_artifact.py` - Domain entity testing
- **Integration Tests**: `tests/test_integration/test_api_integration.py` - API integration testing
- **Repository Tests**: `tests/test_infrastructure/test_db/repositories/test_artifact_repository.py` - Database testing
- **Use Case Tests**: `tests/test_application/test_use_cases/test_process_artifact.py` - Business logic testing

### Adding New Dependencies

The template uses **strict version pinning** for all dependencies. Add new dependencies to `pyproject.toml`:

**For production dependencies:**
```toml
[project]
dependencies = [
    "existing-dependency==1.2.3",
    "new-dependency==2.0.0",  # Use exact version
]
```

**For development dependencies:**
```toml
[dependency-groups]
dev = [
    # Linting and formatting
    "ruff==0.13.1",
    "black==23.0.0",
    "isort==5.12.0",

    # Type checking
    "mypy==1.5.0",
    "types-requests==2.31.0",

    # Testing
    "pytest==8.4.2",
    "pytest-asyncio==0.21.0",
    "pytest-cov==4.1.0",

    # Add new dev dependency
    "new-dev-tool==1.0.0",  # Use exact version
]
```

**Important Notes:**
- Always use exact versions (`==`) for reproducible builds
- Update dependencies manually when needed
- Test thoroughly after dependency updates


## 🤝 Contributing

Want to contribute? Check out our [contribution guide](CONTRIBUTING.md) for guidelines.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) for the powerful ORM
- [Dishka](https://github.com/reagento/dishka) for dependency injection
- [Faststream](https://github.com/ag2ai/faststream) for the convenient work with message brokers
- [Cookiecutter](https://cookiecutter.readthedocs.io/) for project templating

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the documentation
- Review the generated project's README.md

---

**Happy coding! 🚀**
