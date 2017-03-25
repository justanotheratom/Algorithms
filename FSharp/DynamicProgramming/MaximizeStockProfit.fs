﻿
open System
open NUnit.Framework
open FsUnit

module MaximizeStockProfit =

    let maxProfit1 p =
        
        let rec loop minSoFar maxProfitSoFar rest =
            match rest with
            | [] -> maxProfitSoFar
            | h :: t ->
                let newMin =
                    if (h < minSoFar) then h else minSoFar
                let newMaxProfit =
                    let profit = h - minSoFar
                    if (profit > maxProfitSoFar) then profit else maxProfitSoFar
                loop newMin newMaxProfit t

        match p with
        | [] | [_] -> failwith "Not enough datapoints"
        | h :: t -> loop h Int32.MinValue t

    [<Test>]
    let ``Basic Tests`` () =
        let testData =
            [ ([5;3;8;0], 5)
              ([5;4;3;2;1], -1)
              ([1;2;3;4;3;2;1], 3) ]
        testData
        |> List.iter (fun (i, o) -> maxProfit1 i |> should equal o)

    [<Test>]
    let ``Negative Tests`` () =
        let testData =
            [ []
              [2] ]
        testData
        |> List.iter (fun (i) -> (fun () -> maxProfit1 i |> ignore) |> should throw typeof<Exception>)

