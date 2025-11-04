from sqlalchemy.orm import Session
from . import models, schemas

# Users
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def list_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Items
def create_item(db: Session, item: schemas.ItemCreate):
    # ensure owner exists
    owner = get_user(db, item.owner_id)
    if not owner:
        raise ValueError("Owner not found")
    db_item = models.Item(title=item.title, description=item.description, owner_id=item.owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def list_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

# Profiles (one-to-one)
def create_profile(db: Session, profile: schemas.ProfileCreate):
    # ensure user exists and doesn't already have profile
    user = get_user(db, profile.user_id)
    if not user:
        raise ValueError("User not found")
    if user.profile:
        raise ValueError("Profile already exists for this user")
    db_profile = models.Profile(full_name=profile.full_name, address=profile.address, phone=profile.phone, user_id=profile.user_id)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()
