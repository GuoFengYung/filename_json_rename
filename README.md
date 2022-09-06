# Sample_CSV_Data: Cases of config
### contract_data Table1 :
  <div class="tg-wrap"><table>
<thead>
  <tr>
    <th></th>
    <th>用戶1<br>市電 34.87</th>
    <th>用戶2<br>市電 148.14</th>
    <th>用戶3<br>市電 151.28</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>電廠1<br>餘電 34.29</td>
    <td>個別契約1 (60%)<br>綠電 85.71</td>
    <td>🟥共同契約2 (40%)<br>綠電 41.28</td>
    <td>🟥共同契約2 (40%)<br>綠電 38.72</td>
  </tr>
  <tr>
    <td>電廠2<br>餘電 0</td>
    <td>🟦共同契約3 (30%)<br>綠電 29.42</td>
    <td>🟦共同契約3 (30%)<br>綠電 60.58</td>
    <td>個別契約4 (70%)<br>綠電 210</td>
  </tr>
</tbody>
</table></div>

* 用於快速驗證運算模組結果是否正確
* 餘電售價 4.7238, 4.9222，綠電售價 5.124, 6.3, 5.715
* 原始利益為 2,815.058022，第二階段媒合 2816.874102
* Input: origin_config
    ```config
  [
    {
      "power_plant": "電廠1",
      "client": "用戶1",
      "contract_id": "1",
      "percent": 0.6
    },
    {
      "power_plant": "電廠1",
      "client": "用戶2",
      "contract_id": "2",
      "percent": 0.4
    },
    {
      "power_plant": "電廠1",
      "client": "用戶3",
      "contract_id": "2",
      "percent": 0.4
    },
    {
      "power_plant": "電廠2",
      "client": "用戶1",
      "contract_id": "3",
      "percent": 0.3
    },
    {
      "power_plant": "電廠2",
      "client": "用戶2",
      "contract_id": "3",
      "percent": 0.3
    },
    {
      "power_plant": "電廠2",
      "client": "用戶3",
      "contract_id": "4",
      "percent": 0.7
    }
  ]
    ```

### contract_different_time Table2 第一階段:
  <div class="tg-wrap">
    <table>
      <thead>
        <tr>
          <th>Fri. 6am<br>離峰</th>
          <th>用戶1<br>市電: 38.18</th>
          <th>用戶2<br>市電: 17.53 </th>
          <th></th>
          <th>Fri. 7am<br>離峰</th>
          <th>用戶1<br>市電: 20.7</th>
          <th>用戶2<br>市電: 11.79 </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>電廠1</br>餘電:5.71</td>
          <td>個別契約1 (60%)<br>綠電: 30</td>
          <td>個別契約2 (40%)<br>綠電: 14.29</td>
          <td></td>
          <td>電廠1<br>餘電: 12.48</td>
          <td>個別契約1 (60%)<br>綠電: 48</td>
          <td>個別契約2 (40%)<br>綠電: 19.51</td>
        </tr>
        <tr>
          <td>電廠2<br>餘電 0</td>
          <td>🟦共同契約3 (100%)<br>綠電: 31.82</td>
          <td>🟦共同契約3 (100%)<br>綠電: 18.18</td>
          <td></td>
          <td>電廠2<br>餘電 0</td>
          <td>🟦共同契約3 (100%)<br>綠電: 31.3</td>
          <td>🟦共同契約3 (100%)<br>綠電: 18.7</td>
        </tr>
      </tbody>
      <thead>
        <tr>
          <th>Sat. 8am<br>半尖峰</th>
          <th>用戶1<br>市電: 7.92</th>
          <th>用戶2<br>市電: 9.04</th>
          <th></th>
          <th>Sat. 9am<br>半尖峰</th>
          <th>用戶1<br>市電: 0</th>
          <th>用戶2<br>市電: 0</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>電廠1<br>餘電: 16.96</td>
          <td>個別契約1 (60%)<br>綠電: 18.75</td>
          <td>個別契約2 (40%)<br>綠電: 14.29</td>
          <td></td>
          <td>電廠1<br>餘電: 30.13</td>
          <td>個別契約1 (60%)<br>綠電: 11.54</td>
          <td>個別契約2 (40%)<br>綠電: 8.33</td>
        </tr>
        <tr>
          <td>電廠2<br>餘電: 0</td>
          <td>🟦共同契約3 (100%)<br>綠電: 23.33</td>
          <td>🟦共同契約3 (100%)<br>綠電: 26.67</td>
          <td></td>
          <td>電廠2<br>餘電: 19.87</td>
          <td>🟦共同契約3 (100%)<br>綠電: 38.46</td>
          <td>🟦共同契約3 (100%)<br>綠電: 41.67</td>
        </tr>
      </tbody>
    </table>
  </div>

### contract_different_time Table2 第二階段

  <div class="tg-wrap">
    <table style="margin: auto">
      <thead>
        <tr>
          <th>Fri. 6am-7am<br>離峰</th>
          <th>用戶1<br>市電: 58.88</th>
          <th>用戶2<br>市電: 29.35</th>
      </thead>
      <tbody>
        <tr>
          <td>電廠1</br>餘電: 18.19</td>
          <td>媒合: 0</td>
          <td>媒合: 0</td>
        </tr>
        <tr>
          <td>電廠2<br>餘電: 0</td>
          <td>媒合: 0</td>
          <td>媒合: 0</td>
        </tr>
      </tbody>
      <thead>
        <tr>
          <th>Sat. 8am-9am<br>半尖峰</th>
          <th>用戶1<br>市電: 7.92</th>
          <th>用戶2<br>市電: 9.04</th>
      </thead>
      <tbody>
        <tr>
          <td>電廠1<br>餘電: 47.09</td>
          <td>媒合: 0</td>
          <td>媒合: 0</td>
        </tr>
        <tr>
          <td>電廠2<br>餘電: 19.87 - 7.92 - 9.05 = 2.9</td>
          <td>媒合: 7.92</td>
          <td>媒合: 9.05</td>
        </tr>
      </tbody>
    </table>
  </div>

* 用於快速驗證運算模組結果是否正確
* 餘電售價 `4.7238`, `4.9222`，綠電售價 `5.124`, `6.3`
* 原始利益為 ，第二階段媒合: `2634`
* Input: origin_config
    ```config
  [
    {
      "power_plant": "電廠1",
      "client": "用戶1",
      "contract_id": "1",
      "percent": 0.6
    },
    {
      "power_plant": "電廠1",
      "client": "用戶2",
      "contract_id": "2",
      "percent": 0.4
    },
    {
      "power_plant": "電廠2",
      "client": ["用戶1", "用戶2"],
      "contract_id": "3",
      "percent": 1.0
    }
  ]
    ```