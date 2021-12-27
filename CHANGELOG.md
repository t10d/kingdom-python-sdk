# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2021-12-27
### Added
- Database schemas support.
### Removed
- Root Aggregate model.

## [0.3.0] - 2021-11-16
### Added
- Added base implementation of CQRS Pattern.
- Added base implementation of Unit of Work Pattern.
- Added base implementation of Repository Pattern.
- Added base implementation of Message Bus with dependency injection.
- Added base implementation of Redis Message Broker.
- Added higher-order functions to database mappers and factories.
- Added abstract DDD Entity model.
- Added generate now time utility.
- Added root configuration handled by environment variables.
- Added casting to bool from string utility.
- Added json serializer utility.
### Changed
- Renamed project's name from `kingdom-core` to `kingdom-sdk`.
- Increased MyPy rules to be more aggresive.

## [0.2.0] - 2021-10-18
### Added
- Generic start mappers functions to load the ORM.

## [0.1.0] - 2021-10-14
### Added
- Find files utility.
