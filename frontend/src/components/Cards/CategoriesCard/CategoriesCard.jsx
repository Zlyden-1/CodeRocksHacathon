import s from './CategoriesCard.module.scss'
import { NavLink } from "react-router-dom";

export const CategoriesCard = (props) => {
  return (
    <div className={s.wrapper}>
      <div style={{
        backgroundImage: `url(${props.users.photo})`,
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        width: '100%',
        height: '100%',
        borderRadius: '8px',
      }} key={props.users.id}>
        <NavLink to='/listperfomance' className={s.text}>{props.users.name}</NavLink>
      </div>
    </div>
  );
};