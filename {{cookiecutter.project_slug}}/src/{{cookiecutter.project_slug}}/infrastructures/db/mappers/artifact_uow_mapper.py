"""Database mapper for ArtifactModel that implements DbMapperProtocol for Unit of Work.

This mapper provides CRUD operations for ArtifactModel within the Unit of Work pattern.
"""

import logging
from typing import final

from sqlalchemy.ext.asyncio import AsyncSession

from {{cookiecutter.project_slug}}.application.interfaces.db_mapper import DbMapperProtocol
from {{cookiecutter.project_slug}}.infrastructures.db.models.artifact import ArtifactModel

logger = logging.getLogger(__name__)


@final
class ArtifactUoWMapper(DbMapperProtocol[ArtifactModel]):
    """
    Mapper for ArtifactModel that works with Unit of Work pattern.
    
    This mapper handles database operations for ArtifactModel instances
    tracked by the Unit of Work.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    def insert(self, model: ArtifactModel) -> None:
        """Insert a new ArtifactModel into the database."""
        self.session.add(model)
        logger.debug(f"Added ArtifactModel {model.inventory_id} to session")

    def update(self, model: ArtifactModel) -> None:
        """Update an existing ArtifactModel in the database."""
        # The model is already tracked by SQLAlchemy session
        # We just need to ensure it's marked as dirty
        self.session.merge(model)
        logger.debug(f"Merged ArtifactModel {model.inventory_id} into session")

    def delete(self, model: ArtifactModel) -> None:
        """Delete an ArtifactModel from the database."""
        self.session.delete(model)
        logger.debug(f"Deleted ArtifactModel {model.inventory_id} from session")
