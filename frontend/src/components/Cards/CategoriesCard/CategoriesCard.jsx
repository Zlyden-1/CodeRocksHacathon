import s from './CategoriesCard.module.scss'

export const CategoriesCard = (props) => {
    return (
      <div className={s.wrapper}>
        <div style={{ 
          backgroundImage: `url(${props.users.avatar})`, 
          backgroundSize: 'cover', 
          backgroundRepeat: 'no-repeat', 
          backgroundPosition: 'center',
          width: '100%',
          height: '100%',
          borderRadius: '8px',
        }} key={props.users.id}>
        </div>
        <div className={s.text}>{props.users.first_name}</div>
      </div>
    );
  };