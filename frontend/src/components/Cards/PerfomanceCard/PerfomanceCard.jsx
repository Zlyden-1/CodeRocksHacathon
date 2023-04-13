import s from './PerfomanceCard.module.scss'
import { AiFillStar } from 'react-icons/ai'
import { SiGooglemaps } from 'react-icons/si'

export const PerfomanceCard = () => {
  return (
    <div className={s.wrapper}>
      <div className={s.imgcontainer}>
        <div className={s.imgcontent}></div>
        <div className={s.text}><AiFillStar /> 4.5</div>
      </div>
      <div className={s.textcontent}>
        <div className={s.name}>Карла Августина</div>
        <div className={s.name1}><SiGooglemaps />  Самара</div>
        <div>Обладаю большим опытом работы в сфере обучения, как с детьми,
          так и со студентами разных уровней подготовки. Всегда стремлюсь
          найти индивидуальный подход к каждому ученику, учитывая его...</div>
        <div className={s.name2}>
          <div>Индивидуальное обучение английскому языку </div>
          <div>1000$ р/час</div>
        </div>
        <div className={s.name2}>
          <div>Подготовка к экзаменам TOEFL, IELTS </div>
          <div>1300$ р/час</div>
        </div>
      </div>
    </div >
  );
};