import s from './OrderCard.module.scss'
import { TbCalendarTime } from 'react-icons/tb'
import { SiGooglemaps } from 'react-icons/si'

export const OrderCard = () => {
  return (
    <div className={s.wrapper}>
      <div className={s.textcontent}>
        <div className={s.name}>
          <div>Обучение английскому</div>
          <div>1000$-2000$</div>
        </div>
        <div className={s.description}>Я хотел бы найти репетитора по английскому языку для повышения своего уровня владения языком. Я начинающий и имею базовые знания грамматики и лексики. Цель моих занятий - улучшить свой уровень владения языком для быстрой...</div>
        <div className={s.time}>
          <div><TbCalendarTime /> 21.04-15.05</div>
          <div><SiGooglemaps />  Самара</div>
        </div>
        <div className={s.wrapbutton}>
          <div className={s.buttons}>Отредактировать</div>
          <div className={s.buttons2}>Завершить</div>
          <div className={s.buttons3}>Удалить</div>
        </div>
      </div>
    </div>
  );
};