import s from './PerfomanceCard.module.scss'

export const PerfomanceCard = () => {
  return (
    <div className={s.wrapper}>
      <div className={s.imgcontent}>
        <img src='https://mobimg.b-cdn.net/v3/fetch/74/74739e1770f31cdbfdde99cc0b2925d3.jpeg?w=1470&r=0.5625'/>
        <div>Оценка</div>
      </div>
      <div className={s.textcontent}>
        <div>Карла Августина</div>
        <div>Самара</div>
        <div>Карла Августинааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа</div>
        <div>Карла Августина</div>
      </div>
    </div>
  );
};